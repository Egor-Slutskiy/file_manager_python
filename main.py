import os

from file_manager_python import commands
from file_manager_python.commands import Commands


def main():
    file_processing = Commands()
    try:
        current_path = commands.storage.path
        filelist = os.listdir(current_path)
    except Exception:
        print("Неверный путь к папке")
        hasError = True

    while True:
        if hasError:
            break

        command = input("\nВведите команду -> ").split(" ")

        if command[0] == "exit":
            break

        result = file_processing.router(command[0])
        if result:
            try:
                result(*command[1:])
            except TypeError:
                print(f"Некорректные аргументы.")

        else:
            commands_str = "\n".join(
                [
                    f"{key} - {value}"
                    for (key, value) in Commands.get_commands().items()
                ]
            )
            print(f"Команда {command[0]} не найдена. Список команд:\n{commands_str}")

    print("Произведен выход из программы.")


if __name__ == "__main__":
    main()
