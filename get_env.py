import os
import os.path
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

Slack_Bots_APIToken = os.environ.get("Slack_Bots_APIToken")
