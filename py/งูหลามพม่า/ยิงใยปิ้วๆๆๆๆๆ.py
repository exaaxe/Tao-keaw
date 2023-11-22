<<<<<<< HEAD
#webhook embed แบบกล่องข้อความ
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1089135994219008050/7KlI5NFfXvi3PEMYcbyWaArG-EB3r5J1fIFG_nshkaP6Jwk5oircCb6Ed-tdp3k9aVxD')

embed = DiscordEmbed(title='Halo', description='I am banana', color='ffffff')

webhook.add_embed(embed)

=======
#webhook embed แบบกล่องข้อความ
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1089135994219008050/7KlI5NFfXvi3PEMYcbyWaArG-EB3r5J1fIFG_nshkaP6Jwk5oircCb6Ed-tdp3k9aVxD')

embed = DiscordEmbed(title='Halo', description='I am banana', color='ffffff')

webhook.add_embed(embed)

>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
response = webhook.execute()