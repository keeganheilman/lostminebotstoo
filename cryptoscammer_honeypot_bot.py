from scripts.composer import *



if __name__ == "__main__":
    status_update = write_honeypot_tweet()
    send_tweet(status_update)

