import requests

from env_data import bot_token, telegram_id_list


def send_message_tg(order_id: int) -> None:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

        txt = f"Новый заказ №{order_id}"

        for telegram_id in telegram_id_list:

            params = {"chat_id": telegram_id, "text": txt}
            requests.get(url=url, params=params)
