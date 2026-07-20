<%*
// Daily Journal Template - Christina Baldwin "Life's Companion" Style + CBT Integration
// Requires: Templater plugin for Obsidian
// Place in Templates folder, use: <% tp.file.include("daily-journal-template") %>

const today = tp.date.now("YYYY-MM-DD");
const dayName = tp.date.now("dddd");
const time = tp.date.now("HH:mm");
const weekNum = tp.date.now("WW");
const quarter = tp.date.now("Q");
const isoWeek = tp.date.now("YYYY-[W]WW");
%>
---
date: <% today %>
day: <% dayName %>
week: <% weekNum %> (<% isoWeek %>)
quarter: Q<% quarter %>
time: <% time %>
tags: daily-journal, lifes-companion, cbt, attitude-adjustment
tags_daily: <% tp.date.now("YYYY/MM/DD") %>
mood_pre: 
mood_post: 
energy_level: 
tags_daily: 
---

# <% dayName %>, <% today %> | Week <% weekNum %> | Q<% quarter %>

> *"Journal writing is a voyage to the interior." — Christina Baldwin, Life's Companion*

---

## 🌅 Morning Companion (Baldwin's Morning Pages Approach)

### The Opening
*Baldwin: "Begin with the present moment. What is here now?"*

**Right now I notice...** 
> <% tp.file.cursor(1) %>

**Body sensation check-in:**
- Body sensation: 
- Energy level (1-10): 
- Emotional weather: 

**Today's intention** *(Baldwin: "What calls to me today?")*:
> 

### Baldwin's Morning Prompts (choose 1-2)
> *Rotate through these through the week*
- [ ] **Monday - Beginning**: What wants to begin in me today?
- [ ] **Tuesday - Resistance**: What am I resisting? What would happen if I stopped resisting?
- [ ] **Wednesday - Middle**: What is in the middle of unfolding in my life right now?
- [ ] **Thursday - Threshold**: What threshold am I standing at? What's calling me across?
- [ ] **Friday - Completion**: What wants completion this week? What can I release?
- [ ] **Saturday - Sabbath**: What does my soul need to rest from? What needs tending?
- [ ] **Sunday - Sanctuary**: What sanctuary do I need to create or return to today?

**Today's chosen prompt response:**
> 

---

## 🧠 CBT Integration (Burns' Daily Mood Log Integration)

### Pre-Journal Mood Rating
| Mood | Rating (1-10) | Notes |
|------|---------------|-------|
| Sadness | | |
| Anxiety | | |
| Anger | | |
| Guilt/Shame | | |
| Hopelessness | | |
| Loneliness | | |
| **Overall** | | |

### Cognitive Check-In
*Burns TEAM-CBT: "What's the thought? What's the distortion?"*

| Automatic Thought | Distortion(s) | Rational Response | Belief (0-100%) |
|-------------------|---------------|-------------------|-----------------|
| | | | |
| | | | |

**Common Distortions Check** (Burns' 10):
- [ ] All-or-Nothing
- [ ] Overgeneralization
- [ ] Mental Filter
- [ ] Disqualifying Positive
- [ ] Jumping to Conclusions
- [ ] Magnification/Minimization
- [ ] Emotional Reasoning
- [ ] Should Statements
- [ ] Labeling
- [ ] Personalization

---

## 📝 Baldwin's Deepening Prompts (Choose 1-2)

### Dialogue Writing
*Baldwin: "Write a dialogue between parts of yourself"*

**Dialogue: [Part A] ↔ [Part B]**
> **Part A:** 
> 
> **Part B:**
> 
> **Part A:**
> 
> **Part B:**

### Unsent Letter
*To: [person/situation/part of self]*
> 

### List of 100 (Baldwin's technique for deep mining)
*Topic: [e.g., "What I'm grateful for", "What I'm avoiding", "What I want"]*
1. 
2. 
3. 
*(Continue in separate note if flowing)*

### Life Chapter Reflection
*Baldwin: "Where am I in the story of my life?"*
**Current chapter title:** 
**Theme emerging:** 
**Character development:** 

---

## 🎯 Attitude Adjustment Integration (Your Goals Check-in)

### Today's Focus Areas (check 2-3)
- [ ] **Good husband** - One intentional act of connection
- [ ] **Patience** - Notice one trigger, pause, respond vs react
- [ ] **Focus** - One deep work block (90 min), phone away
- [ ] **Mood/Attitude** - One positive reframe, one gratitude
- [ ] **Friend/Colleague** - One reach-out, one appreciation
- [ ] **Leadership/Skills** - One learning, one delegation/mentorship
- [ ] **LLC Alignment** - One action advancing Dunsworth Analytics
- [ ] **Polyglot/Research** - 15 min language/research time

### Today's Commitment (One Thing):
> 

---

## 🌙 Evening Companion (Baldwin's Evening Reflection)

### The Day's Story
*Baldwin: "What happened today? Not the schedule—the story."*

**Three moments that mattered:**
1. 
2. 
3. 

**Where did I feel most alive?**
> 

**Where did I abandon myself?**
> 

**What wants to be remembered?**
> 

### CBT Evening Mood Log
| Mood | Rating (1-10) | Change | Context |
|------|---------------|--------|---------|
| Sadness | | | |
| Anxiety | | | |
| Anger | | | |
| **Overall** | | | |

**Cognitive win today** (one distortion caught & reframed):
> 

**Behavioral experiment result** (if any):
> 

### Gratitude & Meaning (Baldwin + Positive Psychology)
**Three gratitudes (specific, sensory):**
1. 
2. 
3. 

**Meaning moment** (Seligman: "What gave me purpose today?"):
> 

---

## 🔮 Tomorrow's Seed

**Baldwin's evening question:** *"What wants to happen tomorrow through me?"*

**Intention for tomorrow:**
> 

**One small preparation tonight:**
> 

**Dream incubation question** (Baldwin's dreamwork):
> 

---

## 📊 Weekly/Monthly Rollups (Templater: uncomment monthly)
<%*
// Uncomment for weekly review (Sundays)
/*
if (tp.date.now("d") === "0") {
%>

---

## 📅 Weekly Review (Week <% weekNum %>)

**Baldwin's Weekly Questions:**
- What was the theme of this week?
- What chapter am I in?
- What wants completion?
- What wants to begin?

**Goal Progress:**
| Goal | Progress | Note |
|------|----------|------|
| Good husband | | |
| Patience | | |
| Focus | | |
| Mood/Attitude | | |
| Friend/Colleague | | |
| Leadership/Skills | | |
| LLC Alignment | | |
| Polyglot/Research | | |

**CBT Weekly Mood Trend:**
- Average mood: 
- Best day: 
- Challenging day: 
- Key cognitive shift: 

**Gratitude harvest (7):**
1. 2. 3. 4. 5. 6. 7.

**Next week's intention:**
>
<%*
}
%>

---

## 🔗 Links & Connections
- [[<% tp.date.now("YYYY-MM-DD", -1) %>|Yesterday]]
- [[<% tp.date.now("YYYY-MM-DD", 1) %>|Tomorrow]]
- [[Weekly Review <% isoWeek %>]]
- [[Monthly Review <% tp.date.now("YYYY-MM") %>]]
- [[Attitude Adjustment Master Plan]]
- [[Life's Companion - Baldwin Notes]]

---

*Template: Daily Journal - Baldwin's Life's Companion + CBT Integration*
*Template version: 1.0 | Updated: <% tp.date.now("YYYY-MM-DD") %>*
<% tp.file.cursor(2) %>