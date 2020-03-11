# -*- coding:utf-8 -*-

import discord, asyncio, random, time, os
token = "Njg2NDIyNzI1MTkxMDA4MjU4.XmYGdg.43QqoDxiZK7D9BKonvDVH3-xt2Q" # 아까 메모해 둔 토큰을 입력합니다
client = discord.Client() # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.

@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
    
    # discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
    await client.change_presence(status=discord.Status.online, activity=discord.Game("소원 성취"))
    
@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
    
    
    if message.content == "하나코 사랑해":
        rdlove=random.randint(1,3)
        if rdlove==1:
            await message.channel.send("나.. 나는.. 이만 가볼게!!")
        if rdlove==2:
            await message.channel.send("이런 거 좀 곤란한데..")
        if rdlove==3:
            await message.channel.send("... 고마워")   
    if message.content == "하나코 좋아해":
        rdlove=random.randint(1,3)
        if rdlove==1:
            await message.channel.send("이전 부터 말야.. 나도 너가 좋아")
        if rdlove==2:
            await message.channel.send("너라면 받아들일 수 있어.. 나도 좋아해")
        if rdlove==3:
            await message.channel.send("말로 어찌 할수 없을 만큼 나도 네가 좋아")
    if message.content == "하나코 안녕":
            rdhi=random.randint(1,3)
            if rdhi==1 :
                embed = discord.Embed(title="아 너였어?", description="별일 이네. 안녕. 무슨 볼일있어?", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
                embed.set_image(url="https://cdn.discordapp.com/attachments/680300548360241162/686783934402658340/images.png")
                await message.channel.send(embed=embed)
            if rdhi==2 :
                embed = discord.Embed(title="있잖아,", description="계속 있어줘", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
                embed.set_image(url="https://cdn.discordapp.com/attachments/686356380138864662/686784950338322472/D_rOVNiUwAAR3ho.jpg")
                await message.channel.send(embed=embed)
            if rdhi==3 :
                embed = discord.Embed(title="인사?", description="아무렴 어때..", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
                embed.set_image(url="https://cdn.discordapp.com/attachments/686356380138864662/686784193921155102/DScH3oZVQAAQU8a.jpg")
                await message.channel.send(embed=embed)
    if message.content == "하나코 가위":
        rdga=random.randint(1,3)
        if rdga==1:
            embed = discord.Embed(title="비겼네...원한다면 다시 해도 괜찮아", description="(하나코는 가위을 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686512108917096469/images.png")
            await message.channel.send(embed=embed)
        if rdga==2:
            embed = discord.Embed(title="이겼잖아? 하하", description="(하나코는 주먹을 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686511808906919966/R720x0.png")
            await message.channel.send(embed=embed)
        if rdga==3:
            embed = discord.Embed(title="내가 진건가...?", description="(하나코는 보를 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686511954306662478/images.png")
            await message.channel.send(embed=embed)
    if message.content == "하나코 주먹":
        rdga=random.randint(1,3)
        if rdga==1:
            embed = discord.Embed(title="비겼네...원한다면 다시 해도 괜찮아", description="(하나코는 바위를 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686512108917096469/images.png")
            await message.channel.send(embed=embed)
        if rdga==2:
            embed = discord.Embed(title="내가 진건가...?", description="(하나코는 가위를 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686511954306662478/images.png")
            await message.channel.send(embed=embed)
        if rdga==3:
            embed = discord.Embed(title="이겼잖아? 하하", description="(하나코는 보를 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686511808906919966/R720x0.png")
            await message.channel.send(embed=embed)
    if message.content == "하나코 보":
        rdga=random.randint(1,3)
        if rdga==1:
            embed = discord.Embed(title="비겼네...원한다면 다시 해도 괜찮아", description="(하나코는 보를 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686512108917096469/images.png")
            await message.channel.send(embed=embed)
        if rdga==2:
            embed = discord.Embed(title="내가 진건가...?", description="(하나코는 주먹을 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686511954306662478/images.png")
            await message.channel.send(embed=embed)
        if rdga==3:
            embed = discord.Embed(title="이겼잖아? 하하", description="(하나코는 가위를 냈다!)", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.set_image(url="https://cdn.discordapp.com/attachments/683542782484545547/686511808906919966/R720x0.png")
            await message.channel.send(embed=embed)
    if message.content == "하나코 소원":
        await message.channel.send("소원 한가지는 들어줄 수 있어.. 처음이자 마지막이니 신중해지라고?")    
        
        #wish[user.name]=() 
    

client.run(access_token) # 아까 넣어놓은 토큰 가져다가 봇을 실행하라는 부분입니다. 이 코드 없으면 구문이 아무리 완벽해도 실행되지 않습니다.



