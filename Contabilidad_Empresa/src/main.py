from pipeline_movBancarios import pipeline_movBancarios
from pipeline_facturas import pipeline_facturas


def main():

    print("INICIO PIPELINE CONTABILIDAD")

    pipeline_movBancarios()

    pipeline_facturas()

    print("FIN PIPELINE CONTABILIDAD")


if __name__ == "__main__":
    main()