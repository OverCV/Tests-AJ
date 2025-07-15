from src.models.base.application import aplicacion


from src.testing.pruebas_mul import iniciar_pruebas_mul


def main():
    """Inicializar el aplicativo."""

    aplicacion.profiler_habilitado = True
    aplicacion.pagina_sample_network = "A"

    iniciar_pruebas_mul()


if __name__ == "__main__":
    main()
