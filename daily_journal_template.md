---
creation date: <% tp.date.now("YYYY-MM-DD HH:mm") %>
modification date: <% tp.date.now("dddd Do MMMM YYYY HH:mm:ss") %>
author: Dr. Tony Dunsworth
title: Daily Journal <% tp.date.now("YYYY-MM-DD") %>
workday: false
sacred_text_version: <% tp.file.cursor() %>  <%* tR += "%>" %>
sacred_text_phase: <%* 
const phase = await tp.system.suggester(["Phase 1: Excavation", "Phase 2: Articulation", "Phase 3: Embodiment", "Phase 4: Integration", "Phase 5: Evolution", "Not Active"], ["1", "2", "3", "4", "5", "none"], false, "Current Sacred Text Phase?");
if (phase !== "none") tR += phase;
-%>
sacred_text_focus_value: <%* 
const focus = await tp.system.suggester(["Integrity", "Compassion", "Courage", "Wisdom", "Presence", "Integrity/Compassion", "Courage/Wisdom", "Custom"], ["Integrity", "Compassion", "Courage", "Wisdom", "Presence", "Integrity/Compassion", "Courage/Wisdom", "custom"], false, "Today's Sacred Text focus value?");
if (focus === "custom") {
  const custom = await tp.system.prompt("Enter custom focus value:");
  tR += custom;
} else {
  tR += focus;
}
-%>
---
<< [[<% tp.date.now("YYYY-MM-DD", -1) %>]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>]] >>

# <% moment(tp.date.now("YYYY-MM-DD"),'YYYY-MM-DD').format("dddd, MMMM DD, YYYY") %>

## Starting Notes

<%* tp.file.cursor() %>

<%*
const day = tp.date.now("dddd", 0);
const isWeekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"].includes(day);
if (isWeekday) {
  tR += "## ALX Work\n\n";
}
-%>

## DMA Work


## TI Work


## TODO

<%*
// Carry forward unchecked TODOs from previous day
const prevDate = tp.date.now("YYYY-MM-DD", -1);
const prevFile = tp.file.find_tfile(prevDate);
if (prevFile) {
  const prevContent = await tp.file.include(`[[${prevDate}]]`);
  const todoSection = prevContent.split("## TODO")[1];
  if (todoSection) {
    const lines = todoSection.split("\n");
    const unchecked = lines.filter(line => line.trim().startsWith("- [ ]"));
    if (unchecked.length > 0) {
      tR += unchecked.join("\n") + "\n";
    }
  }
}
-%>

- [ ]

## Sacred Text Daily Practice (Bobbi Parish Framework)

### Phase 1: Excavation - Morning Value Intention
- **Today's Focus Value**: `= this.sacred_text_focus_value`
- **Morning Intention**: How will I embody this value today?
- **Excavation Prompt**: What experience yesterday touched this value?

### Phase 3: Embodiment - Daily Ritual Check-in
- [ ] Morning grounding ritual (5 min)
- [ ] Midday values check-in (2 min)
- [ ] Evening alignment review (5 min)
- **Embodiment Note**: How did my body know this value today?

### Phase 4: Integration - Alignment Check
| Life Domain | Alignment (1-10) | Note |
|-------------|------------------|------|
| Marriage/Partnership | | |
| Parenting/Family | | |
| Work/Vocation | | |
| Friendships | | |
| Self-Care | | |
| Leadership | | |

### Phase 5: Evolution - Review Triggers
<%*
const today = tp.date.now("YYYY-MM-DD");
const dateObj = new Date(today);
const month = dateObj.getMonth() + 1;
const day = dateObj.getDate();
// Monthly review trigger
if (day === 1) {
  tR += "\n- [ ] **Monthly Values Audit** (1st of month): Rate alignment 1-10 across domains\n";
}
// Quarterly review trigger
if ((month === 1 || month === 4 || month === 7 || month === 10) && day === 1) {
  tR += "- [ ] **Quarterly Sacred Text Review** (Quarter start): Revise one section\n";
}
// Annual review trigger
if (month === 1 && day === 1) {
  tR += "- [ ] **Annual Sacred Text Revision Ceremony** (Jan 1): Full review & version update\n";
}
-%>

## Daily Mood Log

<%*
const includeMoodLog = await tp.system.suggester(["Yes", "No"], ["Yes", "No"], false, "Include Daily Mood Log?");
if (includeMoodLog === "Yes") {
  tR += "\n" + await tp.file.include("Templates/scripts/daily_mood_log_template_templater.md");
}
-%>

## Project Updates


## Research Projects


## Habit Tracker

<%*
const includeHabitTracker = await tp.system.suggester(["Yes", "No"], ["Yes", "No"], false, "Include Habit Tracker?");
if (includeHabitTracker === "Yes") {
  tR += "\n" + await tp.file.include("Templates/scripts/habit_tracker_template_templater.md");
}
-%>

## Daily Reflection

<%*
const includeReflection = await tp.system.suggester(["Yes", "No"], ["Yes", "No"], false, "Include Daily Reflection?");
if (includeReflection === "Yes") {
  tR += "\n" + await tp.file.include("Templates/scripts/daily_reflection_template_templater.md");
}
-%>

## Daily Tarot Reading - <% tp.date.now("dddd, MMMM DD, YYYY") %>

<%*
const includeTarot = await tp.system.suggester(["Yes", "No"], ["Yes", "No"], false, "Include full Tarot reading template?");
if (includeTarot === "Yes") {
  tR += "\n" + await tp.file.include("Templates/scripts/daily_tarot_reading_template_templater.md");
}
-%>

## Blog Post Ideas

<%*
const includeBlog = await tp.system.suggester(["Yes", "No"], ["Yes", "No"], false, "Include Blog Idea Capture template?");
if (includeBlog === "Yes") {
  tR += "\n" + await tp.file.include("Templates/scripts/blog_idea_capture_template_templater.md");
}
-%>

## Personal Measurements

<%*
const includeMeasurements = await tp.system.suggester(["Yes", "No"], ["Yes", "No"], false, "Include Personal Measurements?");
if (includeMeasurements === "Yes") {
  tR += "\n" + await tp.file.include("Templates/scripts/personal_measurements_template_templater.md");
}
-%>

### Interesting Links.