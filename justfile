default:
  @just --list

run-server:
  uv run litestar --app src.pi_streamdeck.server.app:app run

run-client:
  uv run litestar --app src.pi_streamdeck.client.app:app run
