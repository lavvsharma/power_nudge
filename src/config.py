from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
)

twilio_whatsapp_number = settings["TWILIO_WHATSAPP_NUMBER"]
twilio_account_sid = settings["TWILIO_ACCOUNT_SID"]
twilio_auth_token = settings["TWILIO_AUTH_TOKEN"]

stop_charging_at_percentage = int(settings["STOP_CHARGING_AT_PERCENTAGE"])

whatsapp_message_for_unplug = settings["WHATSAPP_MESSAGE_FOR_UNPLUG"]
receiver_whatsapp_number = settings["RECEIVER_WHATSAPP_NUMBER"]
