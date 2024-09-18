from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-Xqbh3ME7OTg7kbNfifM0LIwg",
  validation_file="file-lDQkbTiYIOTHO7V6ZR5f2AZj",
  model="gpt-4o-2024-08-06",
  integrations=[
        {
            "type": "wandb",
            "wandb": {
                "project": "Leichte SPrache",
            }
        }
    ]
)