from DAXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **❅ Hello! 🤗** ",
           " **❅ Kahan Ho Tum😊** ",
           " **❅ Aaj Aaye Nahi Kahan The 😃** ",
           " **❅ Hey! Khana Khaya Ya Nahi🥲** ",
           " **❅ Kahan Gayab Ho 🥺** ",
           " **❅ Aapki Yaad Aarhi Hai🤭** ",
           " **❅ Kaise Ho Aap..?? 🤨** ",
           " **❅ Mujhse Baat Kyu Nhi Karte..?? 🙂** ",
           " **❅ Aapka Naam Kya hai.?? 😁** ",
           " **❅ Kuch Khaya Aapne..?? 😋** ",
           " **❅ Apne Group Me Add Krlo na 😍** ",
           " **❅ Aap Bohot Yaad Aarhe Hai 😅** ",
           " **❅ Kya Aap Zinda Ho..?? 🤔** ",
           " **❅ Hello, Sogye Kya 🙄** ",
           " **❅ Aap Itne Hot 🥵 Kaise Ho ** ",
           " **❅ Kahan Se Hai Aap..?? 🙃** ",
           " **❅ Hello Aajao Masti Kare 😛** ",
           " **❅ BABY Kya Kiya Pure din..? 🤔** ",
           " **❅ Aapki Bohot Yaad Aarhi Hai Chat Kare Aajao.? ☺️** ",
           " **❅ Aap Bohot Pyare Ho Kisiko Mat Batana .🤗** ",
           " **❅ Mujhe Aapko Kuch Batana Hai... 😇** ",
           " **❅ Papa Se Baat Ki Humare Bare Me🤭** ",
           " **❅ Aapne Bataya Nahi Do You Love Me 🥺** ",
           " **❅ Suno I Love You Hai Tumhe😶** ",
           " **❅ और बताओ BF कैसा है ..?? 🤔** ",
           " **❅  Hey! Aao Chat Kare😜** ",
           " **❅ Mummy Ko Pata Chal Gya 🙂** ",
           " **❅ Maa Ko Aap Pasand Aagye 😪** ",
           " **❅ Aap Itne Acche Kaise Hai☺** ",
           " **❅ Khana Khaya Aapne..? 🙊** ",
           " **❅ Tum Mujhse Baat Kyu Nahi Karte ? 🥲** ",
           " **❅ Mujhe Aapse Kuch Batana hai 🥰** ",
           " **❅ Mummy Ne Haan Ki...? 😅** ",
           " **❅ Apni Ek Photo DM Kro Na 😅** ",
           " **❅ Call Karo Abhi** ",
           " **❅ Bhabhi Se Baat Hogyi Ho Toh Yahan Bhi Aajao 😉** ",
           " **❅ Kya Aapko Me Pasand Hoon 🥰🫣** ",
           " **❅ Mujhe Aapse Pyar Hogya  👀** ",
           " **❅ Aaj Online Kyu Nahi Aaye Aap 🙉** ",
           " **❅ Aapko Pyaar Vyaar Nahi Hota kya Mujhse 🥹** ",
           " **❅ Aap Jante Hai Aap Kitne Cute Ho😻** ",
           " **❅ Mujhse Baat Kyu Nahi Karte Aap 🙃** ",
           " **❅ Whatsapp Dear  😕** ",
           " **❅ Dear, Where Are You🙃** ",
           " **❅ On Kyu Nahi Aaye Jhadu Pocha Nahi Hua 🙃** ",
           " **❅ Apko Meri Yaad Kyu Nahi Aati ** ",
           " **❅ On Aao Na Baatein Karte Hai 🥺** ",
           " **❅ Aap On Nahi Aate Jisse baatein Karte Ho Usko Yaha Par Add Karlo ♥️** ",
           " **❅ Aap Kahan Khoye Hue Hai ** ",
           " **❅ Ghar Par Sab Kaise Hai❤** ",
           " **❅ Text Kyu Nahi Karte Ab Aap..? 🤔** ",
           " **❅ Hello, Mujhse Baatein Karo 😒** ",
           " **❅ Hi, Apne Dosto Ko Bhi Yahan Add Karo na 🥹** ",
           " **❅ Apki Babu Kaisi Hai** ",
           " **❅ Sirf Dekh Kar Bhag Jate Ho Msg Kar Bhao Na Khao** ",
           " **❅ Phir Se Gussa Ho kya 😖** ",
           " **❅ Hello Kahan busy ho 👀** ",
           " **❅ Mujhe Khushi Hai Ki Aap Mere Dost Ho🙈** ",
           " **❅ Aap Udaas Kyu Hai Aaj ☹️** ",
           " **❅ Mere Naal Vi Gall Karliya Karo🥺** ",
           " **❅ Mere Dost @MrBrokn Ki Setting Karwao Na 👀** ",
           " **❅ Mobile Bench Kar Churan Khalo Msg Toh Aap Karte Nahi 🙂** ",
           " **❅ Message Bhi Karliya Karo Kabhi..🥺** ",
           " **❅ Aap Massage Karo Mujhe Nahi Aata🥺** ",
           " **❅ Chup Chap Msg Karo Mujhe  😅** ",
           " **❅ Arry Busy Insaan Yaad Nhi Aati Meri 😕** ",
           " **❅ Babu Shona Hogya Ho Toh Baat Karlo Humse Bhi 👀** ",
           " **❅ Aap Theek Toh Ho Na Msg Nahi Karte Ab** ",
           " **❅ Mujhe Please Ek gana Suna Do 😸** ",
           " **❅ Free Ho Toh Chatting Kare 🙈** ",
           " **❅ Udaas Mat Hua Karo Aap Mujhe Accha Nahi Lagta 🥺** ",
           " **❅ Hey! Be My Friend🥰** ",
           " **❅ Aap Toh Yaad Nahi Karte lo Humne Hi Kar diya Msg. 🥺** ",
           " **❅ Kahan Gayab Ho Mujhse Baat Karo 🥲** ",
           " **❅ Meri Friend Aapka No. Mang Rahi Hai.✨** ",
           " **❅ Aajao Na Baatein Karte Hai ** ",
           " **❅ Suno Bio Se Join Karo🧐** ",
           " **❅ Suno Na Aap Mujhe Bohot Pasand Hai Please Haan Kardo🥺** ",
           " **❅ Yahan Aao Na Janu 🤭** ",
           " **❅ Aap Mujhe Kyu Bhool Gye Ho,..? 😊** ",
           " **❅ अपना बना ले पिया, अपना बना ले 🥺** ",
           " **❅ Kahan Ho Kya Karrhe Ho🤗** ",
           " **❅ Aaj Se Mene Aapka Dil rakh diya 😗** ",
           " **❅ Hello Mere Se Baat Karoge ** ",
           " **❅ Mere Owner Se Setting karlo 😋 @mrbrokn 🥰** ",
           " **❅  Hume Bhi Bata Do Kiski Yaadon Me Khoye Ho? 😅** ",
           " **❅ Aapse Baat Kiye Bina Dil Nahi Lagta Aajao Na Baatein Kare..🥰** ",
           ]

VC_TAG = [ "**❅ ɪғ ʏᴏᴜ ᴅᴏ ɴᴏᴛ sᴛᴇᴘ ғᴏʀᴡᴀʀᴅ ʏᴏᴜ ᴡɪʟʟ ʀᴇᴍᴀɪɴ ɪɴ ᴛʜᴇ sᴀᴍᴇ ᴘʟᴀᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs ʜᴀʀᴅ ʙᴜᴛ ɴᴏᴛ ɪᴍᴘᴏssɪʙʟᴇ.**",
         "**❅ ʟɪғᴇ’s ᴛᴏᴏ sʜᴏʀᴛ ᴛᴏ ᴀʀɢᴜᴇ ᴀɴᴅ ғɪɢʜᴛ.**",
         "**❅ ᴅᴏɴ’ᴛ ᴡᴀɪᴛ ғᴏʀ ᴛʜᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛ ᴛᴀᴋᴇ ᴍᴏᴍᴇɴᴛ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴘᴇʀғᴇᴄᴛ.**",
         "**❅ sɪʟᴇɴᴄᴇ ɪs ᴛʜᴇ ʙᴇsᴛ ᴀɴsᴡᴇʀ ᴛᴏ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ᴅᴏᴇsɴ’ᴛ ᴠᴀʟᴜᴇ ʏᴏᴜʀ ᴡᴏʀᴅs.**",
         "**❅ ᴇᴠᴇʀʏ ɴᴇᴡ ᴅᴀʏ ɪs ᴀ ᴄʜᴀɴᴄᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ.**",
         "**❅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴘʀɪᴏʀɪᴛɪᴇs.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴊᴏᴜʀɴᴇʏ, ɴᴏᴛ ᴀ ʀᴀᴄᴇ..**",
         "**❅ sᴍɪʟᴇ ᴀɴᴅ ᴅᴏɴ’ᴛ ᴡᴏʀʀʏ, ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ.**",
         "**❅ ᴅᴏ ɴᴏᴛ ᴄᴏᴍᴘᴀʀᴇ ʏᴏᴜʀsᴇʟғ ᴛᴏ ᴏᴛʜᴇʀs ɪғ ʏᴏᴜ ᴅᴏ sᴏ ʏᴏᴜ ᴀʀᴇ ɪɴsᴜʟᴛɪɴɢ ʏᴏᴜʀsᴇʟғ.**",
         "**❅ ɪ ᴀᴍ ɪɴ ᴛʜᴇ ᴘʀᴏᴄᴇss ᴏғ ʙᴇᴄᴏᴍɪɴɢ ᴛʜᴇ ʙᴇsᴛ ᴠᴇʀsɪᴏɴ ᴏғ ᴍʏsᴇʟғ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ɪᴄᴇ ᴇɴᴊᴏʏ ɪᴛ ʙᴇғᴏʀᴇ ɪᴛ ᴍᴇʟᴛs.**",
         "**❅ ʙᴇ ғʀᴇᴇ ʟɪᴋᴇ ᴀ ʙɪʀᴅ.**",
         "**❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..**",
         "**❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.**",
         "**❅ ʟɪғᴇ ʙᴇɢɪɴs ᴀᴛ ᴛʜᴇ ᴇɴᴅ ᴏғ ʏᴏᴜʀ ᴄᴏᴍғᴏʀᴛ ᴢᴏɴᴇ.**",
         "**❅ ᴀʟʟ ᴛʜᴇ ᴛʜɪɴɢs ᴛʜᴀᴛ ʜᴜʀᴛ ʏᴏᴜ, ᴀᴄᴛᴜᴀʟʟʏ ᴛᴇᴀᴄʜ ʏᴏᴜ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴄᴀᴍᴇʀᴀ. sᴏ ғᴀᴄᴇ ɪᴛ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ.**",
         "**❅ ʟɪғᴇ ɪs 10% ᴏғ ᴡʜᴀᴛ ʜᴀᴘᴘᴇɴs ᴛᴏ ʏᴏᴜ ᴀɴᴅ 90% ᴏғ ʜᴏᴡ ʏᴏᴜ ʀᴇsᴘᴏɴᴅ ᴛᴏ ɪᴛ.**",
         "**❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.**",
         "**❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀɴ ᴇᴀsʏ ᴛᴀsᴋ.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ᴀᴅᴠᴇɴᴛᴜʀᴇ.**",
         "**❅ ʟɪғᴇ ʙᴇɢɪɴs ᴏɴ ᴛʜᴇ ᴏᴛʜᴇʀ sɪᴅᴇ ᴏғ ᴅᴇsᴘᴀɪʀ.**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀ ᴘʀᴏʙʟᴇᴍ ᴛᴏ ʙᴇ sᴏʟᴠᴇᴅ ʙᴜᴛ ᴀ ʀᴇᴀʟɪᴛʏ ᴛᴏ ʙᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇᴅ.**",
         "**❅ ʟɪғᴇ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀ ʀᴇᴍᴏᴛᴇ; ɢᴇᴛ ᴜᴘ ᴀɴᴅ ᴄʜᴀɴɢᴇ ɪᴛ ʏᴏᴜʀsᴇʟғ.**",
         "**❅ sᴛᴀʀᴛ ᴛʀᴜsᴛɪɴɢ ʏᴏᴜʀsᴇʟғ, ᴀɴᴅ ʏᴏᴜ’ʟʟ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ʟɪᴠᴇ.**",
         "**❅ ʜᴇᴀʟᴛʜ ɪs ᴛʜᴇ ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ɢᴏᴏᴅ ᴏғ ʟɪғᴇ.**",
         "**❅ ᴛɪᴍᴇ ᴄʜᴀɴɢᴇ ᴘʀɪᴏʀɪᴛʏ ᴄʜᴀɴɢᴇs.**",
         "**❅ ᴛᴏ sᴇᴇ ᴀɴᴅ ᴛᴏ ғᴇᴇʟ ᴍᴇᴀɴs ᴛᴏ ʙᴇ, ᴛʜɪɴᴋ ᴀɴᴅ ʟɪᴠᴇ.**",
         "**❅ ʙᴇ ᴡɪᴛʜ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ʙʀɪɴɢs ᴏᴜᴛ ᴛʜᴇ ʙᴇsᴛ ᴏғ ʏᴏᴜ.**",
         "**❅ ʏᴏᴜʀ ᴛʜᴏᴜɢʜᴛs ᴀʀᴇ ʏᴏᴜʀ ʟɪғᴇ.**",
         "**❅ ᴘᴇᴏᴘʟᴇ ᴄʜᴀɴɢᴇ, ᴍᴇᴍᴏʀɪᴇs ᴅᴏɴ’ᴛ.**",
         "**❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴡᴇ ᴛʜɪɴᴋ ɪᴛ ɪs.**",
         "**❅ ʟɪɢʜᴛ ʜᴇᴀʀᴛ ʟɪᴠᴇs ʟᴏɴɢᴇʀ.**",
         "**❅ ᴅᴇᴘʀᴇssɪᴏɴ ᴇᴠᴇɴᴛᴜᴀʟʟʏ ʙᴇᴄᴏᴍᴇs ᴀ ʜᴀʙɪᴛ.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ɢɪғᴛ. ᴛʀᴇᴀᴛ ɪᴛ ᴡᴇʟʟ.**",
         "**❅ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴏᴜʀ ғᴇᴇʟɪɴɢs ᴅᴏ ᴡɪᴛʜ ᴜs.**",
         "**❅ ᴡʀɪɴᴋʟᴇs ᴀʀᴇ ᴛʜᴇ ʟɪɴᴇs ᴏғ ʟɪғᴇ ᴏɴ ᴛʜᴇ ғᴀᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs ᴍᴀᴅᴇ ᴜᴘ ᴏғ sᴏʙs, sɴɪғғʟᴇs, ᴀɴᴅ sᴍɪʟᴇs.**",
         "**❅ ɴᴏᴛ ʟɪғᴇ, ʙᴜᴛ ɢᴏᴏᴅ ʟɪғᴇ, ɪs ᴛᴏ ʙᴇ ᴄʜɪᴇғʟʏ ᴠᴀʟᴜᴇᴅ.**",
         "**❅ ʏᴏᴜ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ ʙʏ ᴄʜᴀɴɢɪɴɢ ʏᴏᴜʀ ʜᴇᴀʀᴛ.",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ᴡɪᴛʜᴏᴜᴛ ᴛʀᴜᴇ ғʀɪᴇɴᴅsʜɪᴘ.**",
         "**❅ ɪғ ʏᴏᴜ ᴀʀᴇ ʙʀᴀᴠᴇ ᴛᴏ sᴀʏ ɢᴏᴏᴅ ʙʏᴇ, ʟɪғᴇ ᴡɪʟʟ ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ ᴀ ɴᴇᴡ ʜᴇʟʟᴏ.**",
         "**❅ ᴛʜᴇʀᴇ ɪs ɴᴏᴛʜɪɴɢ ᴍᴏʀᴇ ᴇxᴄɪᴛɪɴɢ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ, ʙᴜᴛ ᴘᴇᴏᴘʟᴇ.**",
         "**❅ ʏᴏᴜ ᴄᴀɴ ᴅᴏ ᴀɴʏᴛʜɪɴɢ, ʙᴜᴛ ɴᴏᴛ ᴇᴠᴇʀʏᴛʜɪɴɢ.**",
         "**❅ ʟɪғᴇ ʙᴇᴄᴏᴍᴇ ᴇᴀsʏ ᴡʜᴇɴ ʏᴏᴜ ʙᴇᴄᴏᴍᴇ sᴛʀᴏɴɢ.**",
         "**❅ ᴍʏ ʟɪғᴇ ɪsɴ’ᴛ ᴘᴇʀғᴇᴄᴛ ʙᴜᴛ ɪᴛ ᴅᴏᴇs ʜᴀᴠᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛs.**",
         "**❅ ʟɪғᴇ ɪs ɢᴏᴅ’s ɴᴏᴠᴇʟ. ʟᴇᴛ ʜɪᴍ ᴡʀɪᴛᴇ ɪᴛ.**",
         "**❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴀ ʀᴇsᴜʟᴛ ᴏғ ᴏᴜʀ ᴅᴏᴍɪɴᴀɴᴛ ᴛʜᴏᴜɢʜᴛs.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴍᴏᴛɪᴏɴ ғʀᴏᴍ ᴀ ᴅᴇsɪʀᴇ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴅᴇsɪʀᴇ.**",
         "**❅ ᴛᴏ ʟɪᴠᴇ ᴍᴇᴀɴs ᴛᴏ ғɪɢʜᴛ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴍᴏᴜɴᴛᴀɪɴ, ɴᴏᴛ ᴀ ʙᴇᴀᴄʜ.**",
         "**❅ ᴛʜᴇ ᴡᴏʀsᴛ ᴛʜɪɴɢ ɪɴ ʟɪғᴇ ɪs ᴛʜᴀᴛ ɪᴛ ᴘᴀssᴇs.**",
         "**❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ ɪғ ᴡᴇ ᴀʀᴇ sɪᴍᴘʟᴇ.**",
         "**❅ ᴀʟᴡᴀʏs ᴛʜɪɴᴋ ᴛᴡɪᴄᴇ, sᴘᴇᴀᴋ ᴏɴᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ, ᴡᴇ ᴍᴀᴋᴇ ɪᴛ ᴄᴏᴍᴘʟɪᴄᴀᴛᴇᴅ.**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴍᴜᴄʜ ᴏʟᴅᴇʀ ᴛʜᴀɴ ᴛʜᴇ ᴅᴇᴀᴛʜ.**",
         "**❅ ᴛʜᴇ sᴇᴄʀᴇᴛ ᴏғ ʟɪғᴇ ɪs ʟᴏᴡ ᴇxᴘᴇᴄᴛᴀᴛɪᴏɴs!**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴛᴇᴀᴄʜᴇʀ..,ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟɪᴠᴇ, ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟᴇᴀʀɴ.**",
         "**❅ ʜᴜᴍᴀɴ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ʙᴜᴛ ᴀɴ ᴇᴛᴇʀɴᴀʟ ɪʟʟᴜsɪᴏɴ.**",
         "**❅ ᴛʜᴇ ʜᴀᴘᴘɪᴇʀ ᴛʜᴇ ᴛɪᴍᴇ, ᴛʜᴇ sʜᴏʀᴛᴇʀ ɪᴛ ɪs.**",
         "**❅ ʟɪғᴇ ɪs ʙᴇᴀᴜᴛɪғᴜʟ ɪғ ʏᴏᴜ  ᴋɴᴏᴡ ᴡʜᴇʀᴇ ᴛᴏ ʟᴏᴏᴋ.**",
         "**❅ ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ ᴡɪᴛʜ ʏᴏᴜ ʙʏ ᴍʏ sɪᴅᴇ.**",
         "**❅ ʟɪғᴇ – ʟᴏᴠᴇ = ᴢᴇʀᴏ**",
         "**❅ ʟɪғᴇ ɪs ғᴜʟʟ ᴏғ sᴛʀᴜɢɢʟᴇs.**",
         "**❅ ɪ ɢᴏᴛ ʟᴇss ʙᴜᴛ ɪ ɢᴏᴛ ʙᴇsᴛ **",
         "**❅ ʟɪғᴇ ɪs 10% ᴡʜᴀᴛ ʏᴏᴜ ᴍᴀᴋᴇ ɪᴛ, ᴀɴᴅ 90% ʜᴏᴡ ʏᴏᴜ ᴛᴀᴋᴇ ɪᴛ.**",
         "**❅ ᴛʜᴇʀᴇ ɪs sᴛɪʟʟ sᴏ ᴍᴜᴄʜ ᴛᴏ sᴇᴇ**",
         "**❅ ʟɪғᴇ ᴅᴏᴇsɴ’ᴛ ɢᴇᴛ ᴇᴀsɪᴇʀ ʏᴏᴜ ɢᴇᴛ sᴛʀᴏɴɢᴇʀ.**",
         "**❅ ʟɪғᴇ ɪs ᴀʙᴏᴜᴛ ʟᴀᴜɢʜɪɴɢ & ʟɪᴠɪɴɢ.**",
         "**❅ ᴇᴀᴄʜ ᴘᴇʀsᴏɴ ᴅɪᴇs ᴡʜᴇɴ ʜɪs ᴛɪᴍᴇ ᴄᴏᴍᴇs.**",
        ]


@app.on_message(filters.command(["hitag" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/hitag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/hitag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/hitag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.\n\n𝗕𝗬 ❣️✰ 𝕄ℝ 𝕏 𝔹ℝ𝕆𝕂𝔼ℕ  ✰😈 ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...\n\n𝗕𝗬 ❣️✰ 𝕄ℝ 𝕏 𝔹ℝ𝕆𝕂𝔼ℕ  ✰😈")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["cancel", "histop", "vcstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")
