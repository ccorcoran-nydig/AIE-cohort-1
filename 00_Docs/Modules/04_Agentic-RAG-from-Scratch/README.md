# Session 4: 🕴️ Agentic RAG From Scratch

🎯 Goal: Look under the hood of agentic RAG and the create_agent abstraction

📚 **Learning Outcomes**
- Learn the core constructs of low-level orchestration using LangGraph
- Understand how to set up tracing, view traces, and monitor performance
- Understand how to use and locally host the newest open-source LLM and embedding models

🧰 **New Tools**
Orchestration: [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
Inference & Serving: [ollama](https://ollama.com/)

## 📛 Required Tooling & Account Setup
- Download and create an [ollama](https://ollama.com/) account

## 📜 Recommended Reading
- [LangGraph 1.0](https://blog.langchain.com/langchain-langgraph-1dot0/) (Oct 2025)
- [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph), by LangGraph

# 🔁 Introduction to LangChain v1.0
It's important to understand the fundamental shift that took place to build LangChain v1.0. LangGraph was put _underneath_ LangChain, as it's a more fundamental layer. We covered this in our introduction to LangChain v1.0 when it came out, and their CEO Harrison talked about it with his team around the same time. A great story!

<h3 align="center">Agent Engineering with LangChain 1.0 (AI Makerspace)</h3>

<p align="center">
  <a href="https://www.youtube.com/watch?v=lSfAPNJx3xQ">
    <img
      src="https://img.youtube.com/vi/lSfAPNJx3xQ/maxresdefault.jpg"
      alt="Watch the video on YouTube"
      width="50%"
    />
  </a>
</p>

<h3 align="center">Building LangChain and LangGraph 1.0 (LangChain) </h3>

<p align="center">
  <a href="https://www.youtube.com/watch?v=r5Z_gYZb4Ns">
    <img
      src="https://img.youtube.com/vi/r5Z_gYZb4Ns/maxresdefault.jpg"
      alt="Watch the video on YouTube"
      width="50%"
    />
  </a>
</p>

So here we are - it's time to dig under the hood and understand LangGraph! While the concepts of [designing an agent runtime from first principles](https://www.blog.langchain.com/building-langgraph/) are quite interesting, we're going to start focusing a bit more on implementation today, which opens our ability to achieve a lot more complexity and control over that complexity in the production apps we build!


# 🕸️  Core Constructs: LangGraph

Instead of building our entire RAG chain using runnables, the best-practice in 2025 is to use LangGraph directly.

<aside>
🔄 LangGraph lets us **add cycles** to applications built on LangChain.

</aside>

The essence of LangGraph is that it uses graphs to add cycles.  

**Why Cycles?**

We can think of a cycle in our graph as a more robust and customizable loop. It allows us to keep our application ***agent-forward*** while still giving the powerful functionality of traditional loops.

Due to the inclusion of cycles over loops, we can also compose rather complex flows through our graph in a much more readable and natural fashion. Effectively allowing us to recreate application flowcharts in code in an almost 1-to-1 fashion.

**Why LangGraph?**

During this session, *we will be using LangGraph as a Directed Acyclic Graph (DAG*).  Beyond the agent-forward approach - we can easily compose and combine traditional DAG chains with powerful cyclic behavior due to the tight integration with LCEL. 

In this way, LangGraph is a natural extension to LangChain's core offerings!

## Graphs

Graphs are collections of connected objects: nodes and edges.

- **Node**: Think `function` or `runnable`; i.e. *something that changes **state***
- **Edge**: Think path to take; i.e., *where to pass **state** object next*

A state object is initially defined by passing a state definition to a class representing the graph.  This state object, or `StateGraph`, gets updated over time.  The agent's internal state is represented simply as a list of messages.  Remember how we interacted with the OpenAI API with a list of messages with roles?  Same idea.

Just as every component of a chain is a runnable, each node in our graph can be a runnable, or even an entire chain!  

Welcome to the next layer of abstraction.

Do you have any questions about how to best prepare for Session 4 after reading? Please don't hesitate to provide direct feedback to `greg@aimakerspace.io` or `Dr Greg` on Discord!

