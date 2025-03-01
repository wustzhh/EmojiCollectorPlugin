from astrbot.plugin import Plugin
from astrbot.event import MessageEvent
import random


class EmojiCollectorPlugin(Plugin):
	def __init__(self):
		self.emojis = []
	
	async def run(self, event: MessageEvent):
		# 检查是否为群聊消息
		if event.message_type == 'group':
			# 提取消息中的表情
			emojis = [seg.data['file'] for seg in event.message if seg.type == 'image']
			if emojis:
				self.emojis.extend(emojis)
			# 以10%的概率回复一个随机表情
			elif self.emojis and random.random() < 0.1:
				await event.reply([{'type': 'image', 'data': {'file': random.choice(self.emojis)}}])
	
	def info(self):
		return {
			"name": "EmojiCollector",
			"desc": "收集并随机发送群友的表情",
			"help": "自动收集群友发送的表情，并以10%的概率随机发送一个已收集的表情。",
			"version": "1.0",
			"author": "wust_zhh"
		}
