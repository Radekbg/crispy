import os
import sys
from google import genai
from google.genai import errors


class TerminalAIAssistant:

    def __init__(self):
        """Конструктор на класа.

        Инициализира клиента за връзка с Gemini API.
        """
        # Проверяваме дали API ключът е наличен в средата
        if not os.environ.get("GEMINI_API_KEY"):
            print(
                "Грешка: Не е намерен GEMINI_API_KEY в променливите на средата."
            )
            print("Моля, задайте го преди да стартирате програмата. Пример: export GEMINI_API_KEY=<твоят_ключ_тук>")
            sys.exit(1)

        # Инициализираме официалния клиент на Gemini
        # Той автоматично ще вземе ключа от os.environ["GEMINI_API_KEY"]
        self.client = genai.Client()
        # Използваме актуалния и бърз модел gemini-2.5-flash
        self.model_name = "gemini-2.5-flash"

    def get_input(self) -> str:
        """Взима въпрос от потребителя през терминала."""
        print("\n" + "=" * 50)
        user_input = input("Потребител (напишете 'exit' за край): ").strip()
        return user_input

    def send_prompt(self, prompt: str) -> str:
        """Изпраща въпроса към Gemini API и връща отговора."""
        try:
            # Извеждаме съобщение, че се зарежда, за по-добра предвидимост
            print("Мислене...")
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )
            return response.text
        except errors.APIError as e:
            return f"Грешка при комуникацията с API: {e}"
        except Exception as e:
            return f"Възникна неочаквана грешка: {e}"

    def print_output(self, output: str):
        """Принтира отговора от изкуствения интелект в четим формат."""
        print("\n--- Отговор от AI ---")
        print(output)
        print("=" * 50)

    def run(self):
        """Основният цикъл на програмата, който управлява логиката."""
        print("Добре дошли в Terminal AI Assistant!")
        print("Можете да задавате въпроси по всяко време.")

        while True:
            # 1. Взимаме вход от потребителя
            user_question = self.get_input()

            # Изход от програмата, ако потребителят напише 'exit'
            if user_question.lower() == "exit":
                print("Благодаря, че използвахте Terminal AI Assistant. Довиждане!")
                break

            # Пропускаме празни въведени низове
            if not user_question:
                print("Моля, въведете валиден въпрос.")
                continue

            # 2. Изпращаме въпроса към API-то
            ai_response = self.send_prompt(user_question)

            # 3. Принтираме резултата
            self.print_output(ai_response)


# Точка на стартиране на скрипта
if __name__ == "__main__":
    # Създаваме инстанция на нашия ООП клас
    assistant = TerminalAIAssistant()
    # Стартираме асистента
    assistant.run()