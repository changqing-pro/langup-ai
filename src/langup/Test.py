from langup import reaction
from reaction.voice import play_sound
import asyncio

async def test():
    audio_txt = "根据岗位JD，提取岗位要求，在招聘平台上筛选出符合要求的候选人，和他们进行打招呼，和他们交流沟通以获取简历  I'm hosting a live stream about digital recruitment, helping clients find suitable candidates for their job openings"
    tts = reaction.TTSSpeakReaction(audio_txt=audio_txt, block=True)
    path = await tts.areact()
    play_sound(path)

asyncio.run(test())
