from flask import Blueprint, request, jsonify
from datetime import datetime
import requests

from config import db
from reserva.reserva_model import Reserva
from reserva.reserva_model import TurmaNaoEncontrada

reservas_bp = Blueprint('reservas', __name__)

TOTAL_SALAS_DISPONIVEIS = 13  # Define o número de salas disponiveis na escola

@reservas_bp.route('/reservas', methods=['POST'])
def criar_reserva():
    dados = request.get_json()

    try:
        turma_id = dados['turma_id']
        data = datetime.strptime(dados['data'], '%Y-%m-%d').date()
        hora_inicio = datetime.strptime(dados['hora_inicio'], '%H:%M').time()
        hora_fim = datetime.strptime(dados['hora_fim'], '%H:%M').time()
        sala = dados['sala'] 

       
        resposta = requests.get(f'http://localhost:5000/api/turmas/{turma_id}')
        if resposta.status_code != 200:
            raise TurmaNaoEncontrada(f'Turma {turma_id} não encontrada')

        
        conflito = Reserva.query.filter(
            Reserva.data == data,
            Reserva.sala == sala,
            db.or_(
                db.and_(Reserva.hora_inicio <= hora_inicio, Reserva.hora_fim > hora_inicio),
                db.and_(Reserva.hora_inicio < hora_fim, Reserva.hora_fim >= hora_fim),
                db.and_(Reserva.hora_inicio >= hora_inicio, Reserva.hora_fim <= hora_fim)
            )
        ).first()
        if conflito:
            return jsonify({'erro': f'A sala {sala} já está reservada nesse horário'}), 409

        # Verifica se o total de salas já foi utilizado para essa data e hora
        reservas_no_horario = Reserva.query.filter(
            Reserva.data == data,
            db.or_(
                db.and_(Reserva.hora_inicio <= hora_inicio, Reserva.hora_fim > hora_inicio),
                db.and_(Reserva.hora_inicio < hora_fim, Reserva.hora_fim >= hora_fim),
                db.and_(Reserva.hora_inicio >= hora_inicio, Reserva.hora_fim <= hora_fim)
            )
        ).count()
        if reservas_no_horario >= TOTAL_SALAS_DISPONIVEIS:
            return jsonify({'erro': 'Todas as salas estão ocupadas nesse horário'}), 409

        
        nova_reserva = Reserva(
            data=data,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim,
            turma_id=turma_id,
            sala=sala
        )

        db.session.add(nova_reserva)
        db.session.commit()

        return jsonify({'mensagem': 'Reserva criada com sucesso'}), 201

    except TurmaNaoEncontrada as e:
        return jsonify({'erro': str(e)}), 404
    except KeyError as e:
        return jsonify({'erro': f'Campo obrigatório ausente: {str(e)}'}), 400
    except ValueError:
        return jsonify({'erro': 'Formato de data ou hora inválido'}), 400



@reservas_bp.route('/reservas', methods=['GET'])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([reserva.to_dict() for reserva in reservas])
    
    

    