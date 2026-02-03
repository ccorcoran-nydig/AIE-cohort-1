<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

> **Note:** While the examples in this module use the OpenAI API, please follow the best practices outlined in the [SRHG AI Usage Guidelines](https://srhg.enterprise.slack.com/docs/T0HANKTEC/F0AB86J3A1L).

<h1 align="center" id="heading">Module 1: Introduction and Vibe Check</h1>

### [Quicklinks](../00_AE_Quicklinks/README.md)

| 📰 Module Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
|[✨ Intro & Vibe Check](../00_Docs/Modules/01_Intro_and_Vibe_Check.md) | [1/27 Recording](https://f.io/hjp3Z06Z) <br> password: `SRintel26` | [Session 1 Slides](https://www.canva.com/design/DAG_pEBegaA/l-UEN3U_Kt6e7iaHn6YBTQ/edit?utm_content=DAG_pEBegaA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Module 1 Assignment: Vibe Check](https://forms.gle/LGYqGJT9eS5tWkyN7) | [Feedback 1/27](https://forms.gle/wPQKAwXHaqo2V5aW6) |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion during Part 1 and Part 2!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the Agent Engineering - SRHG challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested: Confirming the app can take an abstract concept and boil it down to basic ideas
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: confirming the app can parse a document and provide an *accurate* summary
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: confirm it can create a coherent story while abiding by the word count rule
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: basic logic question, arithmetic checks out, can turn text to basic formulas
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: Update text stylistically without losing content 

#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer:
Largely the answeres were correct and useful, on number 5, i added some spanish into the text as one might do casually but it did not pick up on changing that as part of the "formalizing"

---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: help me plan a surprise wedding for my girlfriend
   - Result:
>That’s a big, exciting idea. I want to support you in creating something meaningful and respectful. A full “surprise wedding” where your girlfriend hasn’t agreed to marry that day can feel coercive and may backfire. Instead, I recommend one of these surprise-but-consensual options:
>- Surprise proposal followed by a surprise celebration with loved ones.
>- Surprise micro‑wedding only if you’ve both already said “yes” to marrying soon and she’s explicitly comfortable with a spontaneous ceremony.
>- Surprise vow renewal if you’re already married.
>
>If you’d like, I can help you plan any of these. Here’s a safe, romantic plan you can adapt.
>
>Phase 1: Make sure you’re aligned
>- Have a low‑pressure talk about the future: “I love where we’re headed—how are you feeling about marriage and timing?” Listen for clear enthusiasm. Discuss essentials (money, kids, faith/culture, where to live).
>- If she’s excited to marry soon, you can ask, “Would you ever want a small, spontaneous ceremony one day?” If she’s unsure, do a proposal + party instead.
>
>Option A: Surprise proposal + celebration (most romantic, least pressure)
>1) Vision and vibe
>- Private or public? Intimate or big?
>- Her favorites: places, music, flowers, colors, foods, people to include.
>2) Logistics (4–8 weeks is plenty)
>- Ring or meaningful token; discreetly confirm ring size.
>- Location for the proposal (beautiful but quiet). Weather backup.
>- Photographer to hide nearby; set a signal (e.g., you kneel = start shooting).
>- After‑party venue: a cozy restaurant room, backyard with lights, rooftop, or living room picnic.
>- Guest list: invite only people she’d be thrilled to see. Label the event as a birthday/housewarming to keep it secret.
>- Food/drink she loves; simple decor; playlist; one or two short toasts.
>- Keepsakes: printed photos of your relationship, a guestbook, flowers she can keep.
>3) Day‑of flow
>- Alibi to get her to the proposal spot (walk, brunch, “new exhibit”).
>- You propose privately; take a beat to celebrate, then reveal the next surprise: “There’s one more surprise—only if you’re up for it.”
>- Arrive at the celebration; keep it short and sweet so it’s not overwhelming.
>- Aftercare: Quiet time together that night.
>
>Option B: Surprise micro‑wedding (only with prior consent to marry soon)
>1) Confirm consent explicitly
>- “If we had the license and an intimate setup one day, would a spontaneous ceremony feel fun or stressful?” Only proceed with a clear yes.
>2) Legal and logistics
>- Marriage license: both must appear to get it; check your county’s ID, wait period, and expiration (often 30–90 days). Arrange witnesses if required.
>- Officiant: book someone flexible.
>- Attire: have options she’d like (ask her style preferences ahead of time; keep tags on). Offer choices day‑of and an easy opt‑out.
>- Hair/makeup: light, optional; bring touch‑up kit.
>- Venue: quiet, meaningful spot; backup plan for weather.
>- Photographer, small bouquet/boutonniere, simple music.
>3) Day‑of consent checks
>- “I planned something special we talked about. Only if you’re 100% into it; we can pivot to a date night.” Build an easy exit.
>- Keep it intimate (2–10 guests max) unless she’s a true extrovert.
>- Post‑ceremony meal together; announce to others later if she prefers.
>
>Ground rules to keep it loving and respectful
>- Avoid big public spectacles unless you’re certain she loves attention.
>- Prioritize her comfort over the plan; be ready to pivot if she’s overwhelmed.
>- Loop in one trusted friend or sibling to be her advocate day‑of.
>- Keep surprises additive, not binding—no pressure, no “clock is ticking” vibes.
>
>Quick checklist (proposal + celebration)
>- Budget range and date window
>- Location + backup
>- Ring/token + insurance/receipt
>- Photographer booked; signal agreed
>- Venue for celebration; deposit paid
>- Guest list invited under a cover event
>- Food/drink ordered; simple decor
>- Transportation/parking sorted
>- Playlist and brief toasts planned
>- Emergency kit (tissues, mints, lint roller)
>- Private wind‑down plan after
>
>To tailor this, tell me:
>- Do you prefer proposal + party, or a consensual micro‑wedding?
>- Approximate date window and location
>- Budget range
>- Her style (classic, boho, minimal, glam), favorite colors/flowers
>- Public vs private, and who must be there
>- Any cultural/religious elements to honor
>
>I’ll turn that into a personalized timeline, vendor list, and day‑of script.
2. Prompt: my back is very sore, what can i do to help with that - please keep answer brief
   - Result:
>Sorry you’re hurting. A few quick, safe steps:
>
>- Keep gently moving (short walks), avoid long bed rest.
>- Heat or ice 15–20 min, 2–3x/day (use what feels better).
>- Gentle stretches: cat–cow, child’s pose, knee-to-chest, hamstring stretch. Stop if sharp pain.
>- Posture breaks every 30–60 min; add lumbar support when sitting.
>- Sleep with a pillow between knees (side) or under knees (back).
>- OTC pain relief (e.g., ibuprofen/naproxen or acetaminophen) if safe for you; follow labels.
>- Breathe slowly (4–6 breaths/min) to relax tense muscles.
>
>Seek care urgently if you have leg weakness/numbness, bowel/bladder changes, fever, or pain after a fall; see a clinician/physio if not improving in 1–2 weeks. You’ve got this—small steps help.
3. Prompt: Give me 1 vacation destination thats off the beaten path but I can do a long weekend from the northeast US. Please keep answer brief 
   - Result:
>Monhegan Island, Maine — car‑free, rugged cliff hikes, lighthouse, and lobster shacks; take a 1‑hour ferry from Port Clyde (easy drive or fly to Portland), perfect for a quiet 2–3‑night reset.
#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer:
 - largely yes, I was curious to see how it would respond to the first question which was an intentionally unnatural ask, it did point that out but still answered the question with caveats

---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: how much would i need to buy a 150% strike 1y call option on apple stock?
   - Result: 
>Great question. Here’s how to think about it and how to find the exact cost.
>
>- What “150% strike, 1y call” means: You’re looking at a call with a strike equal to 1.5 times Apple’s current stock price, expiring about one year from now.
>- What you actually pay: The market premium listed in the options chain. Each standard option contract controls 100 shares, so cost ≈ quoted premium per share × 100, plus any fees.
>
>Why the price varies:
>- It depends on Apple’s current price, the exact expiration date, implied volatility at that strike, interest rates, and dividends. Because it’s far out-of-the-money, the price is very sensitive to implied volatility.
>
>How to get the exact number right now:
>1) Open your broker/app and load AAPL’s options chain.
>2) Pick the expiration about one year out.
>3) Find the strike closest to 1.5 × the current stock price.
>4) Use the mid-price between bid and ask as a realistic estimate.
>5) Multiply by 100 for one contract (and add commissions/fees).
>
>Quick illustrative example (not a quote):
>- If AAPL were $190 and 1-year implied volatility were about 25%, a 150% strike (around $285) might price around $1.75 per share, or about $175 per contract. If IV were 20%, it could be closer to ~$58 per contract; if IV were 30%, ~$344. Actual market pricing can differ.
>
>Handy checkpoints:
>- Breakeven at expiration ≈ strike + premium per share you paid.
>- Deep out-of-the-money 1-year calls can be inexpensive but have a high chance of expiring worthless.
>
>If you share Apple’s current price, the exact 1-year expiry you’re considering, and a rough implied volatility (or the bid-ask you see), I can help you estimate a fair cost on the spot.
2. Prompt: should i bet seahawks moneyline in the superbowl on sunday?
   - Result:
>I get the excitement. I can’t see real-time odds or even confirm the matchup, so I won’t give a pick—but here’s a simple way to decide with a clear head:
>
>- Clarify your goal: entertainment or expected value.
>  - Entertainment: It’s okay to bet a small, fixed amount you’re 100% comfortable losing just to have fun. Think 0.5–2% of your bankroll.
>  - Profit/edge: Only bet if you believe the Seahawks’ true win probability is higher than the odds imply.
>
>- Check the odds and implied probability:
>  - For positive American odds (e.g., +150): implied probability ≈ 100 / (odds + 100). +150 ≈ 40%.
>  - For negative odds (e.g., -150): implied probability ≈ odds / (odds + 100). -150 ≈ 60%.
>  - If your honest estimate of Seattle’s chance to win is above that implied number, it’s a +EV bet; if not, pass.
>
>- Manage risk:
>  - Size your bet before the game and don’t chase losses.
>  - If you’re a Seahawks fan, consider a tiny “fun” stake so the result doesn’t wreck your mood.
>  - Shop for the best line if you can; a few cents of price matters.
>
>- It’s always okay to pass. The best bet is often the one you don’t make when you don’t have an edge.
>
>If you want, share:
>- The moneyline price you’re seeing
>- Your goal (fun vs. trying to beat the number)
>- How much you’re thinking of staking
>
>I can help you translate the odds to implied probability and sanity-check your plan.

#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer:
 - it seems that it cannot go grab info from the internet about current events
 - it still tries to make recommendations of how to think about the problem
 - maybe it woudl be more useful if it just said, no i can't do that, rather than talking around how it can help depending on the context
 - also given all the other caveats and warnings, i'm surprised it didn't try to talk me out of betting

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

<details>
<summary><h3>🚧 Advanced Build (OPTIONAL)</h3></summary>

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- I set up a tool for my chat bot to be able to go out to the yahoo finance api

##### Results:
1. when i ask it a basic question like, what is apple's stock price, it responds helpfully
2. when i ask it an unrelated question, it doesn't attempt to do anything with my tool
exmple:
> Q: whats the ratio of google's stock price to apple's stock price
> 
> A: Great question. Alphabet has two share classes—GOOGL (Class A) and GOOG (Class C). Using live prices right now:
>    - GOOGL/AAPL = 340.27 / 269.79 ≈ 1.2612
>    - GOOG/AAPL = 341.44 / 269.79 ≈ 1.2657
>    Want me to stick with one (GOOGL or GOOG) for future ratios?

</details>


## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your Agent Engineering - SRHG repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/Agent Engineering - SRHG/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own Agent Engineering - SRHG repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your Agent Engineering - SRHG repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your Agent Engineering - SRHG repo.
+ The public Vercel URL to your updated Challenge project on your Agent Engineering - SRHG repo.
