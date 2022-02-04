import matplotlib.pyplot as nurda
users = [4.9, 0.99, 6.1, 3.7, 8, 1.9, 9.32, 2.7, 2.6, 1.901]
users = sorted(users)
language = ["C", "PHP", "CSS", "SQL", "C#", "JS", "Java", "C++", "HTML", "Python"]
index = list(range(len(language)))
nurda.bar(index, users, color="#444444")
nurda.xlabel("Programming languages")
nurda.ylabel("Users in Million")
nurda.xticks(index, language)
nurda.yticks(list(range(len(language) + 1)))
nurda.gca().spines["top"].set_visible(False)
nurda.gca().spines["right"].set_visible(False)
nurda.gca().spines["left"].set_bounds(0, 1000)
for i in users: nurda.annotate(f"{i}M", xy=(users.index(i) - 0.39, i + 0.03))
nurda.title(
    "Number of Users of a Programming Language at SoloLearn, 2021",
    fontweight=10,
    color="#ffffff",
    pad="19.0",
    backgroundcolor="#444444",
    fontdict={
        "horizontalalignment": "center"
    }
)
nurda.savefig("SoloLearn_statistics.png")
nurda.show()
nurda.close()
print("Do you like it? if yes please upvote and tell us your favourite language 😊\n")
