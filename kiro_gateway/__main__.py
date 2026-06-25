def main() -> None:
    import uvicorn
    from main import (
        parse_cli_args,
        validate_configuration,
        resolve_server_config,
        print_startup_banner,
        app,
        UVICORN_LOG_CONFIG,
    )
    from kiro.config import _warn_timeout_configuration

    args = parse_cli_args()
    validate_configuration()
    _warn_timeout_configuration()
    final_host, final_port = resolve_server_config(args)
    print_startup_banner(final_host, final_port)

    uvicorn.run(
        app,
        host=final_host,
        port=final_port,
        log_config=UVICORN_LOG_CONFIG,
    )


if __name__ == "__main__":
    main()
