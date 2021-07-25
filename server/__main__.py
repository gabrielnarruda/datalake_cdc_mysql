from server import stream
from server.services.consumer_api import Consumer
from server.services.utils import enviar_msg_para_canal_suporte


def main():
    try:

        while True:
            consumer = Consumer(stream)
            consumer.consume_stream()
    except Exception as e:
        enviar_msg_para_canal_suporte(e)

    finally:
        stream.close()


if __name__ == "__main__":
    # A Aplicação de modelo Runner consiste em um canal aberto permanentemente com o banco de dados para que os eventos
    # possam ser trafegados em tempo real.
    while True:
        main()
