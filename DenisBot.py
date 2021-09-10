import discord
import time
import random

client = discord.Client()
wordlist = ["네.", "안 됩니다.", "기다려야 합니다.", "나중에 해야 합니다.", "절대 하면 안 됩니다.", "반드시 해야 합니다.", "두 번 하는 것이 좋습니다."]
wordlist2 = ["네.", "아닙니다.", "알 수 없습니다.", "그럴 것 같습니다.", "그럴 겁니다.", "절대 그럴 리 없습니다."]
wordlist_unknown = ["고민해 보겠습니다.", "네.", "그럴 수 없습니다.", "잘 모르겠습니다."]
wordlist_hello = ["예?", "안녕하십니까."]
wordlist_not = ["대부님의 뜻대로...", "저로서는 그 뜻을 이해할 수 없습니다.", "규율대로 집행할 뿐."]

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("'응애'")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    score1=0
    score2=0
    hello=False
    if message.content.startswith("!솔다토"):
        await message.channel.send("…윗사람의 명령에 물음을 구하는 자는 머리통을.")
        time.sleep(1.5)
        await message.delete()
    if message.content.startswith("!카포"):
        await message.channel.send("...")
    if message.content.startswith("!언더보스"):
        if message.content.find("해")!=-1 or message.content.find("할")!=-1:
            score1 +=1
        if message.content.endswith("되죠?"):
            score1 +=100
        if message.content.endswith("되겠나?"):
            score1 +=100
        if message.content.find("제가")!=-1:
            score1 +=1
        if message.content.find("내가") != -1:
            score1 +=1
        if message.content.find("오늘")!=-1:
            score1 +=1
        if message.content.find("내일")!=-1:
            score1 +=1
        if message.content.find("되")!=-1:
            score1 +=1
        if message.content.find("될")!=-1:
            score1 +=1
        if message.content.find("돼")!=-1:
            score1 +=1
        if message.content.find("인")!=-1:
            score2 +=1
        if message.content.find("일")!=-1:
            score2 +=1
        if message.content.find("에")!=-1:
            score2 +=1
        if message.content.find("까")!=-1:
            score2 +=1
        if message.content.find("가")!=-1:
            score2 +=1
        if message.content.find("나")!=-1:
            score2 +=1
        if message.content.find("어")!=-1:
            score2 +=1
        if message.content.find("실크송")!=-1:
            score2 +=1
        if message.content.find("림버스")!=-1:
            score2 +=1
        if message.content=="!언더보스 카포?" or message.content=="!언더보스 데니스?":
            hello=True

        if not message.content.endswith("?"):
            await message.channel.send("'?'를 붙여 주셔야 합니다... 규율입니다.")
        elif hello==True:
            await message.channel.send(wordlist_hello[random.randrange(0,2)])
        elif score1==0 and score2==0:
            await message.channel.send(wordlist_not[random.randrange(0,3)])
        elif score1>score2:
            await message.channel.send(wordlist[random.randrange(0,7)])
        elif score2>score1:
            await message.channel.send(wordlist2[random.randrange(0,6)])
        elif score1==score2:
            await message.channel.send(wordlist_unknown[random.randrange(0,4)])
        




    #따먹 기믹(중요)
    if(message.content.startswith("!언더보스") and message.content.find("따먹") != -1):
        time.sleep(0.3)
        channel = await message.author.create_dm()
        await channel.send("명령이라면 어쩔 수 없지...")
    if(message.content.startswith("!카포") and message.content.find("따먹") != -1):
        time.sleep(0.3);
        channel = await message.author.create_dm()
        await channel.send("이번만이야...")

client.run("ODg1NzM4NTg5MzgyNjY0MjEz.YTraVw.hTMpH8JTdjg69D9r9q_13HuMzGc")
