from bottle import run, get
import glob


@get("/")
def index():
    res = ""
    for file in glob.glob("/home/reox/git/*/.git") + glob.glob("/home/reox/git/*/*/.git"):
        res += file + "<br>"
    return res


if __name__ == "__main__":
    run(host="127.0.0.1", port="8080")
