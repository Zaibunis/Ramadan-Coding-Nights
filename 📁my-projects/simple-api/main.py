from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell products online without handling inventory!",
    "Print on Demand - Create and sell custom designs on merchandise!",
    "Affiliate Marketing - Promote products and earn commissions!",
    "Content Creation - Start a YouTube channel, blog, or podcast!",
    "Virtual Assistant - Provide administrative support remotely!",
    "Tutoring - Teach subjects or skills online for money!",
    "Stock Photography - Sell your photos on platforms like Shutterstock!",
    "Social Media Management - Manage brands' social media accounts!",
    "Handmade Crafts - Sell unique handmade products on Etsy!",
    "App & Web Testing - Get paid to test websites and apps!",
    "Online Surveys - Earn money by sharing your opinions!",
    "Reselling - Buy low-cost items and sell them for profit!",
    "E-book Publishing - Write and sell e-books online!",
    "Voice-over Work - Use your voice for ads, audiobooks, and more!",
    "Gaming - Stream gameplay on Twitch or YouTube for earnings!",
    "Transcription - Convert audio files into written text for pay!"
]

money_quotes = [
    "Wealth consists not in having great possessions, but in having few wants. - Epictetus",
    "The more you learn, the more you earn. - Warren Buffett",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Do what you love and the money will follow. - Marsha Sinetar",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. - Zig Ziglar",
    "If you don’t find a way to make money while you sleep, you will work until you die. - Warren Buffett",
    "The secret of getting ahead is getting started. - Mark Twain",
    "A wise person should have money in their head, but not in their heart. - Jonathan Swift"
]


@app.get("/side_hustles")
def get_side_hustles():
    """Return a random side hustle"""
    return {"side_hustles":random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """Return a random money quote"""
    return {"money_quotes":random.choice(money_quotes)}