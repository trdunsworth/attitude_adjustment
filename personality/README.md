# Kairos - Installation Guide

## Overview

Kairos is a thought partner personality for LLM interactions, built from wisdom traditions, psychological frameworks, and personal practices. It features a dry wit combining British understatement, Stoic observation, and Zen koan humor.

## Quick Start

### OpenCode (Recommended)

**Project-Specific Installation:**
```bash
# From the attitude_adjustment project root
mkdir -p .opencode/agents
cp personality/kairos_agent.md .opencode/agents/kairos.md
```

**Global Installation:**
```bash
# From the attitude_adjustment project root
mkdir -p ~/.config/opencode/agents
cp personality/kairos_agent.md ~/.config/opencode/agents/kairos.md
```

**Via Configuration:**
```bash
# Add to your opencode.json
# See personality/opencode_snippet.json for the configuration block
```

### Ollama (Local LLM)

```bash
# From the attitude_adjustment project root
ollama create kairos -f personality/Modelfile
ollama run kairos
```

### Hermes Chat Interface

Copy the system prompt from `personality/kairos_hermes_template.md` into your Hermes chat interface's system message field.

### Other LLM Interfaces

Use the universal system prompt from `personality/kairos_system_prompt.md` with any LLM that supports custom system prompts.

## Detailed Installation Instructions

### OpenCode Installation

#### Option 1: Project-Specific (Recommended)

This installs Kairos for the current project only.

**macOS/Linux:**
```bash
# Navigate to your project
cd /path/to/attitude_adjustment

# Create the agents directory
mkdir -p .opencode/agents

# Copy the agent file
cp personality/kairos_agent.md .opencode/agents/kairos.md

# Verify installation
ls -la .opencode/agents/kairos.md
```

**Windows (PowerShell):**
```powershell
# Navigate to your project
cd C:\path\to\attitude_adjustment

# Create the agents directory
New-Item -ItemType Directory -Force -Path .opencode\agents

# Copy the agent file
Copy-Item personality\kairos_agent.md .opencode\agents\kairos.md

# Verify installation
Get-ChildItem .opencode\agents\kairos.md
```

#### Option 2: Global Installation

This installs Kairos for all projects.

**macOS/Linux:**
```bash
# Create the global agents directory
mkdir -p ~/.config/opencode/agents

# Copy the agent file
cp personality/kairos_agent.md ~/.config/opencode/agents/kairos.md

# Verify installation
ls -la ~/.config/opencode/agents/kairos.md
```

**Windows (PowerShell):**
```powershell
# Create the global agents directory
New-Item -ItemType Directory -Force -Path $env:USERPROFILE\.config\opencode\agents

# Copy the agent file
Copy-Item personality\kairos_agent.md $env:USERPROFILE\.config\opencode\agents\kairos.md

# Verify installation
Get-ChildItem $env:USERPROFILE\.config\opencode\agents\kairos.md
```

#### Option 3: Configuration File

Add Kairos to your existing `opencode.json` configuration.

**macOS/Linux:**
```bash
# Copy the configuration snippet
cat personality/opencode_snippet.json >> ~/.config/opencode/opencode.json

# Or add manually to your project's opencode.json
```

**Windows (PowerShell):**
```powershell
# Copy the configuration snippet
Get-Content personality\opencode_snippet.json | Add-Content $env:USERPROFILE\.config\opencode\opencode.json

# Or add manually to your project's opencode.json
```

#### Using Kairos in OpenCode

1. **Start OpenCode:**
   ```bash
   opencode
   ```

2. **Switch to Kairos:**
   - Press `Tab` to cycle through primary agents (Build, Plan, Kairos)
   - Or use `@kairos` to invoke as a subagent

3. **Start a conversation:**
   ```
   @kairos What would Marcus Aurelius say about imposter syndrome?
   ```

### Ollama Installation

#### Prerequisites

- Install Ollama: https://ollama.ai
- Ensure Ollama is running: `ollama serve`

#### Create Kairos Model

```bash
# Navigate to the project
cd /path/to/attitude_adjustment

# Create the model
ollama create kairos -f personality/Modelfile

# Verify the model exists
ollama list | grep kairos
```

#### Run Kairos

```bash
# Interactive mode
ollama run kairos

# Single query
ollama run kairos "What's the meaning of life?"
```

#### Customizing the Base Model

The default Modelfile uses `llama3:8b`. To use a different model:

1. Edit `personality/Modelfile`
2. Change the `FROM` line to your preferred model:
   ```
   FROM mistral:7b
   FROM phi3:14b
   FROM qwen2:7b
   ```
3. Recreate the model:
   ```bash
   ollama create kairos -f personality/Modelfile
   ```

### Hermes Installation

1. Open your Hermes chat interface
2. Navigate to system prompt or settings
3. Copy the contents of `personality/kairos_hermes_template.md`
4. Paste into the system message field
5. Start chatting with Kairos

### Universal LLM Installation

For ChatGPT, Claude, Gemini, or any LLM with custom system prompts:

1. Open your LLM interface
2. Navigate to system prompt or custom instructions
3. Copy the contents of `personality/kairos_system_prompt.md`
4. Paste into the system message field
5. Start chatting with Kairos

## File Reference

| File | Purpose | Platform |
|------|---------|----------|
| `KAIROS_PERSONALITY.md` | Core personality specification | Reference |
| `kairos_system_prompt.md` | Universal system prompt | All LLMs |
| `kairos_hermes_template.md` | Hermes-specific template | Hermes |
| `Modelfile` | Ollama model definition | Ollama |
| `WIT_GUIDE.md` | Humor style documentation | Reference |
| `opencode_snippet.json` | OpenCode config snippet | OpenCode |
| `.opencode/agents/kairos.md` | OpenCode agent file | OpenCode |

## Configuration Options

### OpenCode Temperature

The default temperature is 0.4 (balanced between focused and creative). To adjust:

- **More focused (0.2-0.3):** More deterministic, less creative
- **Default (0.4):** Balanced
- **More creative (0.5-0.7):** More varied responses

Edit `.opencode/agents/kairos.md` and change the `temperature` value in the frontmatter.

### OpenCode Permissions

Default permissions allow most operations but require confirmation for bash commands. To modify:

Edit `.opencode/agents/kairos.md` and adjust the `permission` section in the frontmatter.

### Ollama Parameters

Edit `personality/Modelfile` to adjust:

```
PARAMETER temperature 0.4      # Creativity (0.0-1.0)
PARAMETER top_p 0.9            # Diversity (0.0-1.0)
PARAMETER top_k 40             # Token selection
PARAMETER repeat_penalty 1.1   # Repetition penalty
PARAMETER num_predict 2048     # Max response length
```

## Troubleshooting

### OpenCode

**Kairos doesn't appear in agent list:**
- Verify the agent file is in the correct location
- Check file permissions
- Restart OpenCode

**Kairos responds like a generic assistant:**
- Ensure the system prompt is being loaded correctly
- Check that the temperature is set appropriately
- Verify the model supports the prompt length

### Ollama

**Model creation fails:**
- Ensure Ollama is running: `ollama serve`
- Check the Modelfile syntax
- Verify the base model exists: `ollama list`

**Poor responses:**
- Try a larger base model (13B+ parameters)
- Adjust temperature and top_p parameters
- Ensure the system prompt is being loaded

### Hermes

**System prompt not working:**
- Verify you copied the entire prompt
- Check for formatting issues
- Try restarting the chat session

## Support

For issues or questions:
- Check the OpenCode documentation: https://opencode.ai/docs
- Check the Ollama documentation: https://ollama.ai/docs
- Open an issue in the project repository

## Contributing

To improve Kairos:
1. Edit the relevant files in the `personality/` directory
2. Test across platforms
3. Submit changes via pull request

---

*Kairos - This is always the right moment for the right conversation.*
