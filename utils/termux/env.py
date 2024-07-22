from config import ETC


def add_env_variable(key: str, value: str):
    ENV = ETC / "termux-login.sh"
    text = f'export {key}="{value}"\n'
    env = ENV.read_text()
    if text not in env:
        env = env + text
        ENV.write_text(env)
