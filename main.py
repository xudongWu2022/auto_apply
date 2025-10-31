import yaml
from job_sites.indeed_bot import IndeedBot
from utils.logger import get_logger

logger = get_logger("AutoApply")

def load_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    cfg = load_config()
    bot = IndeedBot(
        email=cfg["user"]["email"],
        password=cfg["user"]["password"],
        resume_path=cfg["user"]["resume_path"],
        keywords=cfg["search"]["keywords"],
        location=cfg["search"]["location"]
    )
    bot.run()
