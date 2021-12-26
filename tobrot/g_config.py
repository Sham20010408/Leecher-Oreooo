from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "2132684011:AAGOge2QHLj7yFm8WaA9iyXuPBFC99K9oW4"
    APP_ID = 1424314
    API_HASH = "d1c1c9262bbae8f5eeb80ba47c9f3dff"
    OWNER_ID = 1079261681
    AUTH_CHANNEL = [-1001410465876]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive 
    scope = drive
    root_folder_id =
    token = {"access_token":"ya29.a0ARrdaM-NE9bw7PdiqUtVKYGDX5Re04FX0yntP1gOn42hs2W0OfYkRTjdEfJy9p078vZx5hCfAMCslC0aLjQ4J2BMG2yVJWxTK00BE4tm_e7vU0641B6PaBU4nsaw6YLdNYfrTS8ocXEI5KyJo3fqCKorYtvt","token_type":"Bearer","refresh_token":"1//0gFbg1_2iVKtqCgYIARAAGBASNwF-L9Ir8-H91qYd3AkjmJuSIBSt1RtS-p4h3zkAEcq3ZkSsOMjeDv6GH8Mie7X_uhTa9LLMYD8","expiry":"2021-12-26T12:29:49.4982211-08:00"}
    team_drive = 0AGe_1jbJeQ4PUk9PVA"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
