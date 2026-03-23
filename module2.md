# Module 2: Advanced Design Techniques

In this module, we transition from foundational principles to advanced structural patterns. These techniques are designed to bypass the linear processing limitations of LLMs, enabling them to solve non-trivial reasoning problems through recursive planning and self-correction.

## 2.1 Chain-of-Thought (CoT) and Its Variants

Chain-of-Thought is the practice of encouraging a model to generate intermediate reasoning steps. While simple "Let's think step-by-step" prompts are effective, advanced practitioners use more specialized variants.

### 2.1.1 Self-Consistency (CoT-SC)
Self-consistency involves generating multiple reasoning paths for the same question and then taking the majority vote (most frequent answer).
- **Implementation**: Set `N=5` or `N=10` generations with a non-zero temperature (e.g., T=0.7). Use a secondary prompt or script to parse and tally the results.
- **Use Case**: Mathematical proofs, symbolic reasoning, and complex classification.

### 2.1.2 Least-to-Most Prompting
This technique involves breaking down a complex problem into smaller sub-problems and solving them sequentially, using the output of the previous step as context for the next.
- **Workflow**:
  1. **Decomposition**: "What sub-problems must be solved to answer [Original Question]?"
  2. **Sequential Solving**: Solve Sub-problem 1, then use it to solve Sub-problem 2, etc.
- **Case Study Reference**: Used in technical code refactoring to prevent context loss in large files.

## 2.2 Tree of Thoughts (ToT)

The Tree of Thoughts framework enables LLMs to perform deliberate decision-making by considering multiple different reasoning paths (thoughts) and self-evaluating their promise.

### 2.2.1 The ToT Architecture
1. **Thought Generation**: Generate several potential next steps.
2. **State Evaluation**: Evaluate the likelihood of each step leading to the final goal.
3. **Search Algorithm**: Use Breadth-First Search (BFS) or Depth-First Search (DFS) to explore the "tree" of possibilities.

**Example 2: ToT Strategic Planning Prompt**
```text
<TASK>
Design a go-to-market strategy for a new B2B AI security tool.
</TASK>

<STEP_1_THOUGHT_GENERATION>
Generate three distinct market entry strategies:
1. Direct Sales to G-SIFIs.
2. Product-Led Growth (PLG) for DevOps teams.
3. Channel Partnerships with Cloud Providers.
</STEP_1_THOUGHT_GENERATION>

<STEP_2_EVALUATION>
Evaluate each strategy based on 'Time to Revenue' and 'Market Capture Potential'. Rate each 1-10.
</STEP_2_EVALUATION>

<STEP_3_REFINEMENT>
Select the highest-rated strategy and provide a detailed 90-day execution roadmap.
</STEP_3_REFINEMENT>
```

## 2.3 Dynamic Few-Shot and Semantic Retrieval

Static few-shot examples are often brittle. Production systems should use **Dynamic Few-Shot Selection**.
- **Process**:
  1. User query is embedded using a model (e.g., `text-embedding-3-small`).
  2. A vector database (Pinecone/Milvus) retrieves the 3 most similar examples from a "Gold Dataset."
  3. These retrieved examples are injected into the prompt context.
- **Benefit**: Ensures the model sees examples that are semantically relevant to the specific edge case the user is encountering.

## 2.4 Persona Engineering and Role-Based Prompting

Assigning a persona is more than just "style." It biases the model toward specific technical vocabularies and reasoning patterns.

### 2.4.1 Multi-Agent Personas
Instead of one "expert," use a "committee of experts."
- **Prompt Pattern**: "You are a committee consisting of a CTO, a CISO, and a General Counsel. Review this architecture. Each member must provide a 200-word critique from their perspective. Finally, provide a consolidated recommendation."

## 2.5 Context Window Optimization & Needle Management

With context windows reaching 1M+ tokens (Gemini 1.5/GPT-4o), managing the "Needle-in-a-Haystack" (NIAH) problem is critical.
- **The "Lost-in-the-Middle" Fix**: Place critical instructions and unique identifiers at the very beginning and very end of the context block.
- **Context Distillation**: Before sending 100k tokens to the model, use a smaller, faster model (e.g., GPT-4o-mini) to summarize the irrelevant parts of the context, keeping only the "needles."

---

# Tutorial 1: Building a Recursive Multi-Step Reasoning Pipeline

This tutorial demonstrates how to implement a Python-based pipeline that uses recursive prompting to solve complex technical tasks.

### Step 1: Initialize the Task
We define a complex task: "Analyze a legacy COBOL file and rewrite it in Python using modern async patterns."

### Step 2: The Decomposition Script
```python
import openai

def decompose_task(task_description):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Act as a Lead Software Architect. Break the following task into 3 distinct, executable sub-tasks."},
            {"role": "user", "content": task_description}
        ]
    )
    return response.choices[0].message.content

# Output:
# 1. Parse COBOL logic and identify business rules.
# 2. Map COBOL data structures to Python classes.
# 3. Implement async Python logic for the business rules.
```

### Step 3: Recursive Execution
The script then iterates through these sub-tasks, passing the output of step $N$ as context for step $N+1$.

### Step 4: The Validation Loop
The final step is a "Sanity Check" prompt: "Does the generated Python code maintain 1:1 logic parity with the original COBOL business rules? Provide a line-by-line comparison."

---

## 2.6 Measurable Outcome: Case Study 1
**The Problem**: A global law firm needed to extract clauses from 5,000+ contracts. Zero-shot prompting had a 65% accuracy rate.
**The Solution**: Implementation of CoT-SC (Self-Consistency) with 5 generations per contract.
**The Result**: Accuracy increased to 94%. Latency increased by 4x, but cost was offset by the reduction in manual legal review hours.
