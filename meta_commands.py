import os
import glob
import json


def cmd_list(*args, **kwargs):
    """List all git repositories."""
    pass


def cmd_cd(*args, **kwargs):
    """Change Directory to a given shortname repository."""
    pass


def cmd_tags(*args, **kwargs):
    """Show Tags for a shortname repository."""
    pass


def cmd_find(*args, **kwargs):
    """Find a repository by giving a name, tags or description."""
    pass


def cmd_sync(*args, **kwargs):
    """Generate a List of Repositories and sync with cache file."""
# TODO meh hardcoded...
    repos_raw = glob.glob("/home/reox/git/*/.git") + glob.glob("/home/reox/git/*/*/.git")
    repos = {}

    for repo in repos_raw:
        desc_file = os.path.join(repo, "description")
        if os.path.isfile(desc_file):
            with open(desc_file, "r") as f:
                description = f.read()
                if "unnamed repository" in description.lower():
                    description = ""
        else:
            description = ""

        # parsing tags, they are in the description file

        # assume the shortname is the folder name
        shortname = repo.rsplit("/", 2)[1]
        repos[shortname] = {"description": description, "path": repo}


    with open("metagit_cache.json", "w") as f:
        f.write(json.dumps(repos))
