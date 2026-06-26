# AWS Certified AI Practitioner Slides v19 (p46-75) — Anki Cards
Source: https://media.datacumulus.com/aws-aif/AWS%20Certified%20AI%20Practitioner%20Slides%20v19.pdf · Course: AWS AI Practitioner · Added: 2026-06-26 · src-id: aws-aif-genai-bedrock

> 16 topic cards in deck `Amazon Bedrock` (slides 46–75: *Generative AI with Amazon Bedrock*).

## What is Generative AI
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::what-is-generative-ai`

**Explainer.** Generative AI (Gen-AI) is a subset of deep learning that generates new data similar to its training data — text, images, audio, code, or video. It learns a foundation model pretrained on broad unlabeled data, then adapts it to many downstream tasks.

**Use case.** A single pretrained foundation model can be adapted to text generation, summarization, information extraction, image generation, chatbots, and Q&A.

**Glossary.**
- **Generative AI** — subset of deep learning that creates new data resembling its training data.
- **Foundation Model** — model pretrained on broad unlabeled data, adaptable to many tasks.
- **Pretrain → Adapt** — train once on broad data, then specialize to a task.

**Diagram.** ![What is Generative AI](.transcripts/media/aws-aif-genai-bedrock-what-is-genai.png)

**More details.** Output modalities include text, image, audio, code, and video. The same foundation model supports a broad range of general tasks after adaptation.

## Foundation Models
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::foundation-models`

**Explainer.** A Foundation Model is a large model trained on a wide variety of input data that serves as the base for generative AI. Training one can cost tens of millions of dollars, so most users consume existing FMs rather than train their own.

**Example.** GPT-4o is the foundation model behind ChatGPT.

**Glossary.**
- **Foundation Model (FM)** — broad-data model reused as the base for many generative tasks.

**Diagram.** none

**More details.** There is a wide selection of foundation models from different providers (Amazon, Anthropic, Meta, etc.). To generate data you must rely on an FM.

## Large Language Models (LLMs)
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::large-language-models`

**Explainer.** An LLM is a type of AI designed to generate coherent, human-like text. They are usually very large (billions of parameters) and trained on a large corpus of text such as books, articles, and websites.

**Example.** GPT-4 (ChatGPT / OpenAI) is a notable LLM.

**Glossary.**
- **Large Language Model (LLM)** — AI trained on huge text corpora to produce human-like text.
- **Parameters** — the learned weights; LLMs have billions.

**Diagram.** none

**More details.** Trained on books, articles, websites, and other textual data.

## How LLMs generate text
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::how-llms-generate-text`

**Explainer.** You interact with an LLM via a prompt; it leverages everything it learned to generate new content. It is non-deterministic — the same prompt can yield different text each time, because the next word is sampled from a probability distribution.

**Example.** For “After the rain, the streets were ___” the model lists candidates with probabilities (wet 0.40, flooded 0.25, slippery 0.15…) and randomly selects one based on those probabilities.

**Glossary.**
- **Prompt** — the input text you give the model.
- **Non-deterministic** — output can vary across runs for the same prompt.
- **Token probability** — each candidate next word carries a probability; one is sampled.

**Diagram.** none

**More details.** The model generates a list of potential next words with probabilities, then samples from that list — which is why outputs vary between users.

## Generative AI for Images
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::generative-ai-for-images`

**Explainer.** Generative AI handles images in several directions: generate images from text prompts, transform images from other images, and generate text descriptions from images (multimodal).

**Example.** “Generate a blue sky with the word Hello” (text→image); “Transform this image in anime style” (image→image); “How many apples do you see?” (image→text).

**Glossary.**
- **Text-to-image** — create an image from a text prompt.
- **Image-to-image** — transform one image into another per a prompt.
- **Image-to-text** — describe or answer questions about an image.

**Diagram.** none

**More details.** These multimodal capabilities underpin tools like image generators and visual Q&A.

## Diffusion Models
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::diffusion-models`

**Explainer.** Diffusion models (e.g., Stable Diffusion) generate images from text. Training runs a forward diffusion process that progressively adds noise to a picture; generation runs the reverse process, denoising from random noise toward an image matching the prompt.

**Example.** From the prompt “a cat with a computer,” the reverse diffusion process turns random noise into a matching picture.

**Glossary.**
- **Diffusion Model** — image generator that learns to reverse a noising process.
- **Forward diffusion** — training step that adds noise to images.
- **Reverse diffusion** — generation step that removes noise to form an image.

**Diagram.** ![Diffusion Models](.transcripts/media/aws-aif-genai-bedrock-diffusion-models.png)

**More details.** Stable Diffusion (SDXL) is the canonical example.

## Amazon Bedrock — overview
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::amazon-bedrock-overview`

**Explainer.** Amazon Bedrock is a fully-managed AWS service for building generative AI applications. No servers to manage, pay-per-use pricing, unified APIs across many foundation models, and you keep control of your data (it is not used to train the base model).

**Use case.** Stand up a generative-AI chatbot or document summarizer on AWS without managing servers or training your own model.

**Glossary.**
- **Amazon Bedrock** — fully-managed AWS service to build Gen-AI apps over many FMs.
- **Pay-per-use** — billed by usage, no upfront servers.
- **Unified API** — one API surface across different models.

**Diagram.** none

**More details.** Provides out-of-the-box features and a wide array of foundation models; your data stays under your control.

## Bedrock Foundation Models — private copy & fine-tune
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::bedrock-foundation-models`

**Explainer.** Bedrock gives access to a wide range of foundation models. It makes a private copy of the FM available only to you, which you can further fine-tune with your own data. None of your data is used to train the original FM.

**Use case.** Fine-tune a private copy of Claude on your own support tickets to specialize it — without exposing that data to the base model.

**Glossary.**
- **Private FM copy** — your isolated instance of a foundation model in Bedrock.
- **Fine-tune** — adapt the private copy with your own data.

**Diagram.** none

**More details.** Because the copy is yours, fine-tuning customizes the model without leaking your data into the base model.

## Bedrock components — Playground & Knowledge Bases (RAG)
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::bedrock-components`

**Explainer.** A Bedrock application wires foundation models together with supporting components: an interactive Playground to try models, Knowledge Bases (RAG) that fetch data from your sources for more relevant answers, Fine-tuning to update the model with your data, and a unified API for applications.

**Example.** In the Playground a user selects Anthropic Claude, asks “What’s the most popular dish in Italy?” and gets “Pizza & Pasta.”

**Glossary.**
- **Playground** — interactive UI to test models.
- **Knowledge Bases (RAG)** — retrieval over your data sources to ground responses.
- **RAG** — Retrieval-Augmented Generation: fetch relevant data, then generate.

**Diagram.** ![Bedrock components — Playground & Knowledge Bases (RAG)](.transcripts/media/aws-aif-genai-bedrock-bedrock-components.png)

**More details.** Fine-tuning data and knowledge-base sources commonly live in Amazon S3. The unified API is the same across all models.

## Choosing a Bedrock Foundation Model
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::choosing-a-foundation-model`

**Explainer.** Choose an FM by model type, performance, capabilities, constraints, compliance, level of customization, model size, inference options, licensing, context window, and latency. Multimodal models handle varied input/output types.

**Example.** Amazon Titan (8K ctx), Llama-2 70b (4K), Claude 2.1 (200K), and Stable Diffusion (image gen) differ widely in context window, features, use cases, and price.

**Glossary.**
- **Context window** — max tokens a model can consider at once.
- **Multimodal model** — handles multiple input/output types.
- **Inference options** — how/where the model runs for predictions.

**Diagram.** ![Choosing a Bedrock Foundation Model](.transcripts/media/aws-aif-genai-bedrock-choosing-fm.png)

**More details.** Pricing is per 1K tokens and varies by model (e.g., Titan input $0.0008 / output $0.0016). Pick the trade-off that fits your task and budget.

## Fine-Tuning a Model
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::fine-tuning-a-model`

**Explainer.** Fine-tuning adapts a copy of a foundation model with your own data, changing the base model’s weights. Training data must follow a specific format and be stored in Amazon S3. Not all models can be fine-tuned; re-training needs a higher budget and experienced ML engineers.

**Use case.** Give a chatbot a specific persona/tone, train it on more up-to-date info than the base model knows, or specialize it for a task.

**Glossary.**
- **Fine-tuning** — adapt an FM by updating its weights on your data.
- **Weights** — the model’s learned parameters that fine-tuning changes.

**Diagram.** none

**More details.** Supervised fine-tuning is usually cheaper (less intensive compute, less data). You must prepare/format the data and store it in S3.

## Supervised Fine-Tuning
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::supervised-fine-tuning`

**Explainer.** Supervised Fine-Tuning (SFT) improves a model’s performance on specific tasks by further training it on a particular field using labeled examples — input-output pairs.

**Example.** A labeled pair: {"prompt": "Who is Stéphane Maarek?", "completion": "..."}.

**Glossary.**
- **Supervised Fine-Tuning (SFT)** — fine-tuning on labeled input-output pairs.
- **Labeled example** — an input paired with its desired output.

**Diagram.** none

**More details.** Effectively further trains the model on a particular area of knowledge.

## Reinforcement Fine-Tuning
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::reinforcement-fine-tuning`

**Explainer.** Reinforcement Fine-Tuning (RFT) improves an FM using feedback-based learning. You provide input prompts and define a Reward Function that scores the model’s generated outputs to judge which responses are good. Objective tasks can use AWS Lambda to compute rewards.

**Example.** For a support chatbot, given “My app is running very slowly,” a judge scores candidate replies (e.g., “Restart the app” = helpful but superficial → lower score) to steer toward empathetic, diagnostic answers.

**Glossary.**
- **Reinforcement Fine-Tuning (RFT)** — fine-tuning driven by reward scores on generated outputs.
- **Reward Function** — rule or model that scores output quality.
- **SFT vs RFT** — SFT provides the correct output; RFT scores generated outputs and learns from the scores.

**Diagram.** ![Reinforcement Fine-Tuning](.transcripts/media/aws-aif-genai-bedrock-sft-vs-rft.png)

**More details.** In SFT both input and output are provided; in RFT the model generates multiple outputs that are scored (e.g., 5.0, 2.0, 9.0) to guide learning.

## Distillation
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::distillation`

**Explainer.** Distillation makes models smaller and faster — up to ~75% cheaper than the original — by transferring knowledge from a larger “teacher” model to a smaller “student” model. There is some accuracy decrease, but it is often acceptable.

**Use case.** Distill a large model into a smaller student to cut inference cost up to ~75% for high-volume, latency-sensitive serving.

**Glossary.**
- **Distillation** — compress a model by training a small student from a large teacher.
- **Teacher / Student** — the large source model / the smaller trained model.

**Diagram.** none

**More details.** You provide input data (e.g., prompts) to produce the student model.

## Model Evaluation — Automatic & Human
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::model-evaluation`

**Explainer.** Bedrock evaluates a model two ways. Automatic Evaluation uses built-in task types (summarization, Q&A, classification, open-ended generation) with your own or built-in prompt datasets. Human Evaluation has a work team (employees or subject-matter experts) rate outputs using defined metrics.

**Use case.** Run automatic evaluation for fast quality control, then add human/SME review for nuanced or high-stakes outputs.

**Glossary.**
- **Automatic Evaluation** — built-in, dataset-driven quality scoring.
- **Human Evaluation** — people rate outputs via defined metrics.
- **SME** — Subject-Matter Expert who can judge domain answers.

**Diagram.** none

**More details.** Both use the same built-in task types; human eval adds team selection and custom metrics.

## Benchmark Datasets & Automated Metrics
- Deck: `Amazon Bedrock` · Tags: `src::aws-aif-genai-bedrock` `topic::benchmark-datasets-and-metrics`

**Explainer.** Benchmark datasets are curated data collections built specifically to evaluate model performance across many topics and complexities, measuring accuracy, speed/efficiency, and scalability. Automated metrics score outputs without humans — e.g., ROUGE for summarization and translation.

**Example.** ROUGE-N counts matching n-grams between reference and generated text; ROUGE-L uses the longest common subsequence.

**Glossary.**
- **Benchmark Dataset** — curated data for measuring model performance.
- **ROUGE** — Recall-Oriented Understudy for Gisting Evaluation; scores summaries/translations.
- **ROUGE-N / ROUGE-L** — n-gram overlap / longest-common-subsequence variants.

**Diagram.** none

**More details.** Some benchmark datasets specifically probe particular linguistic phenomena. Automated metrics give fast, repeatable scoring.
