import csv
import logging
import time
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def create_user(user, max_retries=3):
    """Create user with retry logic."""
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(BASE_URL, json=user, timeout=10)

            if response.status_code in (200, 201):
                logging.info(f"User created: {user['email']}")
                return True

            logging.warning(
                f"Attempt {attempt} failed for {user['email']} "
                f"(status={response.status_code})"
            )

        except Exception as e:
            logging.error(f"Attempt {attempt} error for {user['email']}: {e}")

        time.sleep(1)

    return False


def load_users():
    users = []
    with open("users.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                users.append({
                    "name": row["name"].strip(),
                    # "age": int(row["age"]),
                    "email": row["email"].strip()
                })
            except Exception as e:
                logging.error(f"Invalid row: {row} | {e}")

    return users


def verify_users(expected_users):
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()

    api_users = response.json()

    api_emails = {u["email"] for u in api_users}

    missing = []

    for user in expected_users:
        if user["email"] not in api_emails:
            missing.append(user["email"])

    if missing:
        logging.error(f"Verification failed. Missing users: {missing}")
    else:
        logging.info("Verification successful. All users found.")


def main():
    logging.info("Pipeline Test")
    users = load_users()

    success_count = 0

    for user in users:
        if create_user(user):
            success_count += 1

    logging.info(f"Created {success_count}/{len(users)} users")

    # verify_users(users)
try: 
    users = load_users()
    verify_users(users)
except requests.exceptions.HTTPError as e:
    logging.error(f"Verification failed: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
