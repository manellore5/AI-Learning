# AWS Certified AI Practitioner — Glossary
Course: AWS AI Practitioner · Added: 2026-06-30 · src-id: aws-aif-glossary

> 409 unique terms (deduped from all 154 topic cards, slides 47–355) packed into 85 cards (4–5 terms each), across 8 sub-decks under `AWS Certified AI Practitioner::Glossary`. Each card's front lists the term names; the back gives definitions.


## Amazon Bedrock — 77 terms in 16 cards

**Card 1:** Action Group · Agent · Amazon Aurora PostgreSQL · Amazon Bedrock · Amazon Neptune Analytics

- **Action Group** — set of pre-defined actions (often Lambda + OpenAPI schema) an agent can invoke.
- **Agent** — orchestrates multi-step tasks using an FM’s reasoning.
- **Amazon Aurora PostgreSQL** — relational DB option for vectors.
- **Amazon Bedrock** — fully-managed AWS service to build Gen-AI apps over many FMs.
- **Amazon Neptune Analytics** — graph DB enabling GraphRAG.

**Card 2:** Amazon OpenSearch Service · Amazon S3 Vectors · ARPU · Augmented Prompt · Automated metrics

- **Amazon OpenSearch Service** — search/analytics DB with fast nearest-neighbor (kNN) vector search, scales to millions of embeddings.
- **Amazon S3 Vectors** — cost-effective durable vector storage with sub-second queries.
- **ARPU** — Average Revenue Per User attributed to the Gen-AI app.
- **Augmented Prompt** — original query + retrieved text fed to the FM.
- **Automated metrics** — ROUGE, BLEU, BERTScore score outputs without humans.

**Card 3:** Automatic Evaluation · Batch · Benchmark Dataset · Blocked Topics · Chain of Thought

- **Automatic Evaluation** — built-in, dataset-driven quality scoring.
- **Batch** — multiple predictions at once, output a single S3 file, up to 50% discount.
- **Benchmark Dataset** — curated data for measuring model performance.
- **Blocked Topics** — subjects the model is configured to refuse.
- **Chain of Thought** — step-by-step reasoning the agent uses to decide actions.

**Card 4:** CloudWatch Alarm · ContentFilteredCount · Context window · Conversion Rate · Cross-Domain Performance

- **CloudWatch Alarm** — alert built on top of a metric.
- **ContentFilteredCount** — Bedrock metric showing how often content was filtered (Guardrails health).
- **Context window** — max tokens the model can attend to in one generation.
- **Conversion Rate** — share of interactions that reach a desired outcome (e.g. purchase).
- **Cross-Domain Performance** — ability to perform tasks across different domains.

**Card 5:** Data Source connectors · Diffusion Model · Distillation · Domain Adaptation Fine-tuning · Embedding

- **Data Source connectors** — Amazon S3, Confluence, Microsoft SharePoint, Salesforce, web pages (more added over time).
- **Diffusion Model** — image generator that learns to reverse a noising process.
- **Distillation** — compress a model by training a small student from a large teacher.
- **Domain Adaptation Fine-tuning** — train on a domain dataset (most intensive).
- **Embedding** — numerical vector representation of an input.

**Card 6:** Fine-tune · Fine-tuning · Forward diffusion · Foundation Model (FM) · Generative AI

- **Fine-tune** — adapt the private copy with your own data.
- **Fine-tuning** — adapt an FM by updating its weights on your data.
- **Forward diffusion** — training step that adds noise to images.
- **Foundation Model (FM)** — model pretrained on broad unlabeled data, adaptable to many tasks.
- **Generative AI** — subset of deep learning that creates new data resembling its training data.

**Card 7:** Guardrail · High dimensionality · Human Evaluation · Image-to-image · Image-to-text

- **Guardrail** — policy layer controlling FM inputs/outputs.
- **High dimensionality** — many vector components, each capturing a feature.
- **Human Evaluation** — people rate outputs via defined metrics.
- **Image-to-image** — transform one image into another per a prompt.
- **Image-to-text** — describe or answer questions about an image.

**Card 8:** Inference options · Instruction-based Fine-tuning · Knowledge Base · Knowledge Bases (RAG) · Labeled example

- **Inference options** — how/where the model runs for predictions.
- **Instruction-based Fine-tuning** — fine-tune on specific instructions (needs compute).
- **Knowledge Base** — Bedrock-managed store that indexes your data as vector embeddings.
- **Knowledge Bases (RAG)** — retrieval over your data sources to ground responses.
- **Labeled example** — an input paired with its desired output.

**Card 9:** Large Language Model (LLM) · Main cost driver · Model Invocation Logging · Multimodal model · Non-deterministic

- **Large Language Model (LLM)** — AI trained on huge text corpora to produce human-like text.
- **Main cost driver** — number of input + output tokens.
- **Model Invocation Logging** — logs of all Bedrock invocations sent to CloudWatch Logs + S3.
- **Multimodal model** — handles multiple input/output types.
- **Non-deterministic** — output can vary across runs for the same prompt.

**Card 10:** Nova Canvas / Reel · Nova Premier/Pro/Lite/Micro · Nova Sonic · On-Demand · Parameters

- **Nova Canvas / Reel** — image / video generation.
- **Nova Premier/Pro/Lite/Micro** — understanding models from most capable to lowest-latency text-only.
- **Nova Sonic** — conversational speech understanding & generation.
- **On-Demand** — no commitment; text billed per input/output token, embeddings per input token, images per image generated.
- **Parameters** — the learned weights; LLMs have billions.

**Card 11:** Pay-per-use · PII · Playground · Pretrain → Adapt · Private FM copy

- **Pay-per-use** — billed by usage, no upfront servers.
- **PII** — Personally Identifiable Information, which guardrails can remove.
- **Playground** — interactive UI to test models.
- **Pretrain → Adapt** — train once on broad data, then specialize to a task.
- **Private FM copy** — your isolated instance of a foundation model in Bedrock.

**Card 12:** Prompt · Prompt Engineering · Provisioned Throughput · RAG · Reinforcement Fine-Tuning (RFT)

- **Prompt** — the input text you give the model.
- **Prompt Engineering** — no training, no extra compute; cheapest.
- **Provisioned Throughput** — buy model units for 1–6 months to guarantee max tokens/minute.
- **RAG** — Retrieval-Augmented Generation: retrieve relevant data, then generate.
- **Reinforcement Fine-Tuning (RFT)** — fine-tuning driven by reward scores on generated outputs.

**Card 13:** Reverse diffusion · Reward Function · ROUGE · ROUGE-N / ROUGE-L · Semantic similarity

- **Reverse diffusion** — generation step that removes noise to form an image.
- **Reward Function** — rule or model that scores output quality.
- **ROUGE** — Recall-Oriented Understudy for Gisting Evaluation; scores summaries/translations.
- **ROUGE-N / ROUGE-L** — n-gram overlap / longest-common-subsequence variants.
- **Semantic similarity** — related words/inputs sit close together in vector space.

**Card 14:** SFT vs RFT · SME · Subword tokenization · Supervised Fine-Tuning (SFT)

- **SFT vs RFT** — SFT provides the correct output; RFT scores generated outputs and learns from the scores.
- **SME** — Subject-Matter Expert who can judge domain answers.
- **Subword tokenization** — split some words into smaller pieces.
- **Supervised Fine-Tuning (SFT)** — fine-tuning on labeled input-output pairs.

**Card 15:** Teacher / Student · Temperature / Top K / Top P · Text-to-image · Token

- **Teacher / Student** — the large source model / the smaller trained model.
- **Temperature / Top K / Top P** — sampling settings with NO impact on pricing.
- **Text-to-image** — create an image from a text prompt.
- **Token** — the unit (word or subword) an LLM processes.

**Card 16:** Token probability · Unified API · Weights · Word-based tokenization

- **Token probability** — each candidate next word carries a probability; one is sampled.
- **Unified API** — one API surface across different models.
- **Weights** — the model’s learned parameters that fine-tuning changes.
- **Word-based tokenization** — split text into individual words.


## Prompt Engineering — 19 terms in 4 cards

**Card 1:** Chain-of-Thought (CoT) · Context · Drivers · Few-Shot / One-Shot · Input Data

- **Chain-of-Thought (CoT)** — break the task into reasoning steps; combinable with zero/few-shot.
- **Context** — external information that guides the model.
- **Drivers** — model size, model type, input token count, output token count.
- **Few-Shot / One-Shot** — provide a few / one example to guide output.
- **Input Data** — the input you want a response for.

**Card 2:** Instructions · Latency · Length · Mitigation · Negative Prompting

- **Instructions** — the task: what to do and how to perform it.
- **Latency** — response time of the model.
- **Length** — max answer length.
- **Mitigation** — explicit guardrail text instructing the model to ignore out-of-scope or redirecting instructions.
- **Negative Prompting** — instructing the model on undesired content/behavior.

**Card 3:** Output Indicator · Prompt Injection · Prompt Template · Stop Sequences · System Prompt

- **Output Indicator** — the desired output type/format.
- **Prompt Injection** — malicious input that redirects or overrides the intended prompt.
- **Prompt Template** — a reusable prompt skeleton with placeholders for variable parts.
- **Stop Sequences** — tokens that signal the model to stop.
- **System Prompt** — defines how the model should behave/reply.

**Card 4:** Temperature (0–1) · Top K · Top P (0–1) · Zero-Shot

- **Temperature (0–1)** — creativity/randomness of output.
- **Top K** — limit to the K most probable words.
- **Top P (0–1)** — sample from the smallest set of words whose probabilities sum to P.
- **Zero-Shot** — no examples; rely on the model’s general knowledge (better with larger FMs).


## Amazon Q — 18 terms in 4 cards

**Card 1:** Admin Controls · Amazon Q Apps · Amazon Q Business · Code companion · Custom Plugins

- **Admin Controls** — Q Business guardrails.
- **Amazon Q Apps** — no-code, natural-language Gen-AI app builder within Q Business.
- **Amazon Q Business** — managed Gen-AI workplace assistant over company data.
- **Code companion** — real-time code suggestions across Java, JavaScript, Python, TypeScript, C#, etc.
- **Custom Plugins** — connect any 3rd-party app via APIs.

**Card 2:** Data Connectors · Global vs topic-level controls · IAM Identity Center · IDE Extensions · IdP

- **Data Connectors** — fully managed RAG connectors to 40+ enterprise data sources.
- **Global vs topic-level controls** — org-wide rules vs more granular per-topic rules.
- **IAM Identity Center** — AWS service for centralized authentication/SSO.
- **IDE Extensions** — integrate Q into VS Code / Visual Studio for completion, generation, security scans.
- **IdP** — external Identity Provider (Google, Microsoft AD) that can back Identity Center.

**Card 3:** PartyRock · Plugins · Q for AWS Chatbot · Q for EC2

- **PartyRock** — no-account, no-code Gen-AI playground on Bedrock.
- **Plugins** — let Q interact with 3rd-party services (Jira, ServiceNow, Zendesk, Salesforce).
- **Q for AWS Chatbot** — Q inside Slack/Teams Chatbot for AWS troubleshooting.
- **Q for EC2** — instance-type guidance for a workload.

**Card 4:** Q for Glue · Q for QuickSight · Routine actions · Software agent

- **Q for Glue** — help with the ETL service: chat, code generation, job troubleshooting.
- **Q for QuickSight** — NL questions and visual generation over dashboards.
- **Routine actions** — tasks Q can perform (submit time-off, send meeting invites).
- **Software agent** — implements features, generates docs, bootstraps projects.


## AI & Machine Learning — 93 terms in 19 cards

**Card 1:** 1−Specificity · Accuracy · Action / State / Reward · AI · Alignment

- **1−Specificity** — false positive rate.
- **Accuracy** — = (TP + TN) / (TP + TN + FP + FN).
- **Action / State / Reward** — choice / current situation / feedback.
- **AI** — umbrella term for techniques that mimic human intelligence.
- **Alignment** — making outputs match human wants/needs.

**Card 2:** Anomaly Detection · Application Layer · Approximation · Association Rule Learning · AUC

- **Anomaly Detection** — flag outliers (Isolation Forest).
- **Application Layer** — serve model capabilities to users.
- **Approximation** — ML’s inherent output for such problems (a worse fit).
- **Association Rule Learning** — find items that co-occur (Apriori).
- **AUC** — area under the ROC curve (0–1).

**Card 3:** Balanced · Batch inference · Batch size · BERT · BERT / GPT

- **Balanced** — generalizes well.
- **Batch inference** — bulk, offline, accuracy-focused.
- **Batch size** — examples per iteration.
- **BERT** — Bidirectional Encoder Representations from Transformers; reads text both directions.
- **BERT / GPT** — notable transformer-based models.

**Card 4:** Bias · Binary / Multiclass / Multi-label · Classification · Clustering · Data augmentation

- **Bias** — systematic error; high bias = underfitting.
- **Binary / Multiclass / Multi-label** — two classes / many classes / multiple labels per item.
- **Classification** — discrete categorical output.
- **Clustering** — group similar points (K-means); used for segmentation/recommenders.
- **Data augmentation** — synthesize variations to diversify data.

**Card 5:** Data dimensions · Data Layer · Deterministic problem · Downstream task · Early stopping

- **Data dimensions** — labeled/unlabeled and structured/unstructured.
- **Data Layer** — collect vast amounts of data.
- **Deterministic problem** — has an exact, computable solution.
- **Downstream task** — the real end goal the representation is used for.
- **Early stopping** — halt training before it overfits.

**Card 6:** EDA · Edge device · Ensembling · Environment · Epoch

- **EDA** — Exploratory Data Analysis (graphs, correlation matrix).
- **Edge device** — low-power device near the data source.
- **Ensembling** — combine multiple models for accuracy.
- **Environment** — the system it interacts with.
- **Epoch** — one full pass over the training data.

**Card 7:** Expert System · F1 · Feature Extraction · Feature Selection · Feature Transformation

- **Expert System** — rule-based AI (e.g. MYCIN); AI but not ML.
- **F1** — = 2·Precision·Recall / (Precision + Recall).
- **Feature Extraction** — derive useful info (e.g. age from birth date).
- **Feature Selection** — keep the relevant subset of features.
- **Feature Transformation** — reshape data (e.g. normalization).

**Card 8:** GAN · Garbage in, garbage out · GPT · GPU · Hidden Layers

- **GAN** — Generative Adversarial Network; generates synthetic data.
- **Garbage in, garbage out** — poor data yields a poor model.
- **GPT** — Generative Pre-trained Transformer; generates text/code.
- **GPU** — Graphical Processing Unit required for training.
- **Hidden Layers** — intermediate layers that learn patterns.

**Card 9:** Hierarchy · Hyperparameter · Inferencing · k-NN · KPI

- **Hierarchy** — AI ⊃ ML ⊃ Deep Learning ⊃ Generative AI.
- **Hyperparameter** — pre-training setting (vs learned parameters/weights).
- **Inferencing** — making predictions on new data.
- **k-NN** — K-Nearest Neighbors classification algorithm.
- **KPI** — success metric defined by stakeholders.

**Card 10:** Labeled Data · Learning rate · LLM (remote) · Machine Learning · MAE

- **Labeled Data** — inputs + known outputs; used for Supervised Learning.
- **Learning rate** — size of weight-update steps.
- **LLM (remote)** — powerful model accessed via API over the internet.
- **Machine Learning** — learn patterns from data instead of coding rules.
- **MAE** — Mean Absolute Error.

**Card 11:** MAPE · Mapping function · ML Framework/Algorithm Layer · ML Problem Framing · Modality

- **MAPE** — Mean Absolute Percentage Error.
- **Mapping function** — what the model learns to predict outputs.
- **ML Framework/Algorithm Layer** — choose frameworks to solve the use case.
- **ML Problem Framing** — convert a business problem to an ML problem; decide if ML even fits.
- **Modality** — a data type (text, image, audio, video).

**Card 12:** Model Layer · Multi-modal Model · Neural Network · Overfitting · Policy

- **Model Layer** — implement and train the model.
- **Multi-modal Model** — handles multiple input AND output modalities.
- **Neural Network** — connected nodes in layers (can be billions of nodes).
- **Overfitting** — learns noise; fails to generalize.
- **Policy** — JSON of Effect/Action/Resource (+ optional Principal/Condition).

**Card 13:** Precision · Pretext task · Pseudo-labeling · Real-Time inference · Recall

- **Precision** — correct positives vs all predicted positives.
- **Pretext task** — a self-generated training task (e.g. predict masked tokens).
- **Pseudo-labeling** — the model assigns labels to unlabeled data for re-training.
- **Real-Time inference** — fast, per-request (e.g. chatbots).
- **Recall** — correct positives vs all actual positives.

**Card 14:** Regression · Representation · ResNet · Reward Model · RLHF

- **Regression** — continuous output within a range.
- **Representation** — learned encoding of the data.
- **ResNet** — Residual Network (deep CNN); image recognition/detection.
- **Reward Model** — learns to estimate which response a human prefers.
- **RLHF** — Reinforcement Learning from Human Feedback.

**Card 15:** RMSE · RNN · R² (R-squared) · Self-Attention · Semi-supervised Learning

- **RMSE** — Root Mean Squared Error.
- **RNN** — Recurrent Neural Network; sequential data (time-series, speech).
- **R² (R-squared)** — variance explained; close to 1 = good.
- **Self-Attention** — weighs relative importance of words in a sentence.
- **Semi-supervised Learning** — small labeled + large unlabeled data.

**Card 16:** Sensitivity · SLM · Supervised Learning · SVM · Sweet spot

- **Sensitivity** — true positive rate.
- **SLM** — Small Language Model run locally on the edge.
- **Supervised Learning** — train on labeled input→output pairs.
- **SVM** — Support Vector Machine; classification & regression.
- **Sweet spot** — low bias, low variance.

**Card 17:** Tabular Data · Test Set · Text/Image Data · TF-IDF · Time Series Data

- **Tabular Data** — rows = records, columns = features.
- **Test Set** — evaluate final performance (10–20%).
- **Text/Image Data** — common unstructured types.
- **TF-IDF** — text-to-numeric technique.
- **Time Series Data** — points recorded over successive times.

**Card 18:** Training Set · Transformer · Two flavors · Underfitting

- **Training Set** — train the model (typically 60–80%).
- **Transformer** — architecture that processes whole sequences with self-attention.
- **Two flavors** — Regression (numeric) and Classification (categorical).
- **Underfitting** — too simple to capture the pattern.

**Card 19:** Unlabeled Data · Validation Set · Variance · WaveNet

- **Unlabeled Data** — inputs only; used for Unsupervised Learning.
- **Validation Set** — tune parameters/hyperparameters (10–20%).
- **Variance** — sensitivity to the training set; high variance = overfitting.
- **WaveNet** — generates raw audio waveforms (speech synthesis).


## AWS Managed AI Services — 45 terms in 9 cards

**Card 1:** A2I · Amazon Comprehend · Amazon Kendra · Amazon Personalize · Amazon Textract

- **A2I** — Augmented AI: human-in-the-loop review of ML predictions.
- **Amazon Comprehend** — managed NLP for insights in text.
- **Amazon Kendra** — ML document search with NL queries.
- **Amazon Personalize** — managed real-time recommendation service.
- **Amazon Textract** — document text/data extraction service.

**Card 2:** Amazon Translate · ASR · AWS Inferentia · AWS Trainium · Comprehend Medical

- **Amazon Translate** — managed neural machine translation.
- **ASR** — Automatic Speech Recognition.
- **AWS Inferentia** — ML chip optimized for inference.
- **AWS Trainium** — ML chip optimized for deep-learning training.
- **Comprehend Medical** — NLP for clinical text.

**Card 3:** Confidence threshold · Content Moderation · Custom Classification · Custom Entity Recognition · Custom Labels

- **Confidence threshold** — decides which predictions need human review.
- **Content Moderation** — detect inappropriate/offensive content (DetectModerationLabels API).
- **Custom Classification** — sort docs into your own classes.
- **Custom Entity Recognition** — extract business-specific terms/phrases.
- **Custom Labels** — train a custom image classifier from your labeled images.

**Card 4:** Custom Language Model · Custom Moderation Adaptor · Custom Vocabulary · DetectPHI API · EC2

- **Custom Language Model** — trained on domain text for context.
- **Custom Moderation Adaptor** — your labeled images to improve moderation accuracy.
- **Custom Vocabulary** — hints for specific words/acronyms.
- **DetectPHI API** — finds PHI in text.
- **EC2** — rent virtual machines (IaaS).

**Card 5:** Forms & tables extraction · Fulfillment · HealthScribe · HIPAA · Incremental Learning

- **Forms & tables extraction** — structured key-value and tabular output.
- **Fulfillment** — the Lambda action that completes the intent.
- **HealthScribe** — generates clinical notes from conversations.
- **HIPAA** — US health-data privacy regulation.
- **Incremental Learning** — improves results from user feedback.

**Card 6:** Intent · Knowledge Index · Lexicon · Localization · Managed AI Service

- **Intent** — what the user wants to do.
- **Knowledge Index** — the ML-powered index Kendra builds from your sources.
- **Lexicon** — defines how specific text is read aloud.
- **Localization** — adapting content for a target language/region.
- **Managed AI Service** — pre-trained, ready-to-use ML service.

**Card 7:** Mechanical Turk · NER · NLP · PHI · Real-time vs Async

- **Mechanical Turk** — on-demand human task marketplace.
- **NER** — extract predefined general entities.
- **NLP** — Natural Language Processing.
- **PHI** — Protected Health Information.
- **Real-time vs Async** — single synchronous doc vs batch asynchronous.

**Card 8:** Recipe · Redaction · Regional coverage · Reward · Sentiment analysis

- **Recipe** — a pre-packaged algorithm for a specific recommendation use case.
- **Redaction** — automatic removal of PII.
- **Regional coverage** — deployed across multiple AZs/regions for availability.
- **Reward** — the per-task price you set for workers.
- **Sentiment analysis** — how positive/negative text is.

**Card 9:** Slot · Speaker role identification · Speech Marks · SSML · Transcribe Medical

- **Slot** — an input parameter the bot collects to fulfill an intent.
- **Speaker role identification** — distinguishes clinician vs patient.
- **Speech Marks** — encode where words/sentences start/end in the audio.
- **SSML** — Speech Synthesis Markup Language for pronunciation control.
- **Transcribe Medical** — HIPAA-compliant medical speech-to-text.


## Amazon SageMaker — 44 terms in 9 cards

**Card 1:** AMT · Approval status · Asynchronous · AutoML / Autopilot · Batch Transform

- **AMT** — Automatic Model Tuning.
- **Approval status** — gate controlling which version deploys.
- **Asynchronous** — large payloads/long jobs via a queue and S3.
- **AutoML / Autopilot** — automatically builds a custom model.
- **Batch Transform** — predictions over an entire dataset.

**Card 2:** Bias detection · Canvas · Clarify · ClarifyCheck / QualityCheck · Confirmation bias

- **Bias detection** — statistical measurement of bias in data/models.
- **Canvas** — no-code visual ML builder (part of Studio).
- **Clarify** — evaluation, explainability, and bias-detection tool.
- **ClarifyCheck / QualityCheck** — drift checks against baselines.
- **Confirmation bias** — favoring info that confirms preconceptions (mostly human decisions).

**Card 3:** Data Wrangler · DeepAR · Drift · Early stop · End-to-end

- **Data Wrangler** — visual data prep & feature engineering tool.
- **DeepAR** — built-in time-series forecasting algorithm (RNN-based).
- **Drift** — degradation as live data diverges from training data.
- **Early stop** — abandon poor tuning runs to save cost.
- **End-to-end** — collect/prepare → build/train → deploy/monitor in one service.

**Card 4:** Feature · Feature Store · Foundation Model hub · Ground Truth · Ground Truth Plus

- **Feature** — a model input variable.
- **Feature Store** — central repository for storing, transforming, and sharing features.
- **Foundation Model hub** — browse/experiment/customize/deploy flow.
- **Ground Truth** — human-in-the-loop labeling & feedback service.
- **Ground Truth Plus** — managed labeling offering.

**Card 5:** JumpStart · K-means · KNN · Measurement bias · MLFlow

- **JumpStart** — model hub + pre-built ML solution templates.
- **K-means** — clustering to find groupings in data.
- **KNN** — K-Nearest Neighbors for classification.
- **Measurement bias** — flawed/skewed measurement tools.
- **MLFlow** — open-source ML lifecycle management tool.

**Card 6:** Model Card · Model Dashboard · Model Explainability · Model Monitor · Model Registry

- **Model Card** — documentation of a model’s intended uses, risks, and training.
- **Model Dashboard** — central repository/portal of all models.
- **Model Explainability** — tools to explain how a model makes predictions.
- **Model Monitor** — production model-quality monitoring with alerts.
- **Model Registry** — versioned catalog of ML models.

**Card 7:** Network Isolation mode · Objective Metric · Observer bias · PCA · Pipeline

- **Network Isolation mode** — no outbound internet access for job containers.
- **Objective Metric** — the metric AMT optimizes.
- **Observer bias** — the data collector’s personal bias affects results.
- **PCA** — Principal Component Analysis; reduces the number of features.
- **Pipeline** — automated build/train/deploy ML workflow (CI/CD).

**Card 8:** Quick Model · Real-time Endpoint · Role Manager · SageMaker · SageMaker Studio

- **Quick Model** — fast model to sanity-check feature usefulness.
- **Real-time Endpoint** — one prediction at a time, always on.
- **Role Manager** — defines persona-based access roles.
- **SageMaker** — managed end-to-end ML platform.
- **SageMaker Studio** — unified ML development interface.

**Card 9:** Sampling bias · Serverless · Step · Tracking Server

- **Sampling bias** — training data doesn’t represent the population fairly.
- **Serverless** — scales to zero between spikes; cold starts.
- **Step** — a single task in the pipeline.
- **Tracking Server** — records runs/experiments.


## Responsible AI & Governance — 66 terms in 14 cards

**Card 1:** AI Governance Board · AI Service Card · Algorithm accountability · Amplified decision-making · Black-box model

- **AI Governance Board** — cross-functional oversight committee.
- **AI Service Card** — AWS responsible-AI documentation for an AI service.
- **Algorithm accountability** — algorithms should be transparent and explainable.
- **Amplified decision-making** — AI augments rather than replaces human judgment.
- **Black-box model** — model whose internals are hard to interpret (e.g. neural nets).

**Card 2:** Cataloging · Complexity/Opacity · Compliance · Continuous Retraining · Data Integrity

- **Cataloging** — organizing/documenting datasets.
- **Complexity/Opacity** — hard to audit how decisions are made.
- **Compliance** — adherence to regulations/guidelines.
- **Continuous Retraining** — periodically retrain on new data.
- **Data Integrity** — complete, consistent, error-free data with backups/audit trails.

**Card 3:** Data Lineage · Data Logging · Data origin documentation · Data Residency · Data Retention

- **Data Lineage** — the documented origin and transformation history of data.
- **Data Logging** — track inputs/outputs/metrics/events.
- **Data origin documentation** — dataset sources, licenses, known biases/quality issues.
- **Data Residency** — where data is processed/stored (regulation/privacy).
- **Data Retention** — how long data is kept (regulatory/cost).

**Card 4:** Data Steward/Owner/Custodian · Data Wrangler bias fix · Decision Tree · Dynamism · Emergent Capabilities

- **Data Steward/Owner/Custodian** — defined data-governance roles.
- **Data Wrangler bias fix** — augment underrepresented groups to balance data.
- **Decision Tree** — branching rule-based supervised model.
- **Dynamism** — systems change over time, not static.
- **Emergent Capabilities** — unintended abilities.

**Card 5:** Explainability · Exposure · F1-score · Fairness · GDPR

- **Explainability** — explain behavior via inputs/outputs without internal detail.
- **Exposure** — model leaks sensitive training data.
- **F1-score** — balanced average of precision and recall.
- **Fairness** — promote inclusion, prevent discrimination.
- **GDPR** — EU data protection.

**Card 6:** Governance · Governance / Safety / Controllability · Guardrail model · Guardrails · Hallucination

- **Governance** — policies/oversight to manage AI risk and value.
- **Governance / Safety / Controllability** — enforce practices / benefit society / align to human intent.
- **Guardrail model** — filters unwanted content.
- **Guardrails** — Bedrock content/PII/topic controls.
- **Hallucination** — plausible-sounding but false generated claim.

**Card 7:** HCD · Hijacking / Prompt Injection · Infrastructure Protection · Interpretability · Jailbreaking

- **HCD** — Human-Centered Design.
- **Hijacking / Prompt Injection** — embedded prompt instructions override behavior.
- **Infrastructure Protection** — access control, segmentation, encryption.
- **Interpretability** — understand the internal cause of a decision.
- **Jailbreaking** — bypass safety constraints.

**Card 8:** Least privilege · MLOps · Nondeterminism · PCI DSS · PDP

- **Least privilege** — grant only the access needed.
- **MLOps** — operational practices to deploy/monitor/retrain ML systematically.
- **Nondeterminism** — same prompt can yield different outputs.
- **PCI DSS** — payment-card data security.
- **PDP** — Partial Dependence Plot.

**Card 9:** PETs · Plagiarism/Cheating · Poisoning · Privacy & Security · Probability sampling

- **PETs** — Privacy-Enhancing Technologies (masking, obfuscation, encryption, tokenization).
- **Plagiarism/Cheating** — Gen-AI used for essays/applications; hard to trace LLM output sources, spurring AI-detection tools.
- **Poisoning** — malicious data added to training.
- **Privacy & Security** — individuals control if/when data is used.
- **Probability sampling** — the root cause: LLMs sample the next token.

**Card 10:** Prompt Leaking · Reflexivity · Regulated Workload · Responsible AI · Review Cadence

- **Prompt Leaking** — accidental disclosure of prompts/inputs.
- **Reflexivity** — reflecting on the decision process.
- **Regulated Workload** — work subject to regulatory audit/archival/security requirements.
- **Responsible AI** — transparent, trustworthy, risk-mitigating AI across the lifecycle.
- **Review Cadence** — scheduled technical/legal/responsible-AI reviews.

**Card 11:** Scope 1–5 · Security (CIA) · Security IN the Cloud · Security OF the Cloud

- **Scope 1–5** — Consumer App, Enterprise App, Pre-trained, Fine-tuned, Self-trained — increasing ownership.
- **Security (CIA)** — confidentiality, integrity, availability.
- **Security IN the Cloud** — customer responsibility (data, access, config).
- **Security OF the Cloud** — AWS responsibility (infrastructure).

**Card 12:** Shared controls · SOC / ISO / NIST · Source Citation · Split

- **Shared controls** — patch management, configuration management, awareness & training.
- **SOC / ISO / NIST** — controls/standards frameworks.
- **Source Citation** — attributing data sources and their licenses.
- **Split** — a feature-value rule that divides the data.

**Card 13:** Threat Detection · Toxicity · Trade-off · Transparency

- **Threat Detection** — spot fake content, manipulated data, automated attacks.
- **Toxicity** — offensive/inappropriate generated content.
- **Trade-off** — more interpretability often means less performance.
- **Transparency** — openness about the system.

**Card 14:** Transparency Standards · Veracity & Robustness · Version control · Vulnerability Management

- **Transparency Standards** — publishing model/training/decision info + feedback channels.
- **Veracity & Robustness** — reliable even in unexpected situations.
- **Version control** — track and roll back data/code/models.
- **Vulnerability Management** — find/patch software and model weaknesses.


## AWS Security Services — 47 terms in 10 cards

**Card 1:** Artifact Agreements · Artifact Reports · Audit Manager · Availability · AWS Config

- **Artifact Agreements** — review/accept AWS agreements (e.g. BAA/HIPAA).
- **Artifact Reports** — downloadable security/compliance reports (ISO, PCI, SOC).
- **Audit Manager** — assess/audit compliance with automated evidence collection.
- **Availability** — readiness to access (varies by storage class).
- **AWS Config** — record/audit resource configuration & compliance over time.

**Card 2:** AWS PrivateLink · Bucket · CloudTrail · CloudTrail with Bedrock · Compliance rule

- **AWS PrivateLink** — technology powering most interface endpoints.
- **Bucket** — region-level container with a globally unique name.
- **CloudTrail** — records account API calls/events for audit.
- **CloudTrail with Bedrock** — audit Bedrock API calls (e.g. who invoked ListCustomModels).
- **Compliance rule** — desired config the resource is checked against.

**Card 3:** CVE · Durability · EBS / ELB / ASG · EC2 User Data · Framework

- **CVE** — known vulnerability database Inspector checks against.
- **Durability** — probability an object is not lost (11 nines, all classes).
- **EBS / ELB / ASG** — block storage / load balancer / auto-scaling group.
- **EC2 User Data** — boot-time bootstrap script (runs once, as root).
- **Framework** — prebuilt or custom set of compliance controls.

**Card 4:** GB-second · Glacier (Instant/Flexible/Deep Archive) · IAM Role · IAM with Bedrock · Inspector

- **GB-second** — billing unit = RAM × duration.
- **Glacier (Instant/Flexible/Deep Archive)** — low-cost archival; retrieval times/min-durations vary.
- **IAM Role** — grants Bedrock access to S3 + KMS.
- **IAM with Bedrock** — access control to Bedrock resources.
- **Inspector** — automated vulnerability assessment (EC2, ECR, Lambda).

**Card 5:** Intelligent-Tiering · Internet Gateway · ISV · KMS Key · Lambda

- **Intelligent-Tiering** — auto-tiers by usage for a small monitoring fee.
- **Internet Gateway** — connects public subnets to the internet.
- **ISV** — Independent Software Vendor.
- **KMS Key** — managed encryption key (needs decrypt permission for Bedrock).
- **Lambda** — serverless FaaS, auto-scaling, event-driven.

**Card 6:** Languages · Macie · Multi-part upload · NAT Gateway · Object Key

- **Languages** — Node.js, Python, Java, C#, Ruby, custom runtimes.
- **Macie** — ML-based sensitive-data (PII) discovery for S3.
- **Multi-part upload** — required for objects over 5 GB (max object 5 TB).
- **NAT Gateway** — outbound internet for private subnets.
- **Object Key** — full path = prefix + object name.

**Card 7:** One Zone-IA · Private Subnet · PrivateLink with Bedrock · Risk score · Role

- **One Zone-IA** — one AZ; data lost if the AZ is destroyed.
- **Private Subnet** — no direct internet access.
- **PrivateLink with Bedrock** — private VPC access to Bedrock.
- **Risk score** — prioritization value per vulnerability.
- **Role** — permissions assumed by a service (EC2, Lambda, CloudFormation).

**Card 8:** S3 Gateway Endpoint · Security Group · Security Group / Endpoint Policy · Six categories

- **S3 Gateway Endpoint** — private S3 access (there’s also an S3 Interface Endpoint).
- **Security Group** — instance firewall rules.
- **Security Group / Endpoint Policy** — control who/what can use the endpoint.
- **Six categories** — Cost, Performance, Security, Fault Tolerance, Service Limits, Operational Excellence.

**Card 9:** SSE-KMS · Standard-IA · Subnet · Trail

- **SSE-KMS** — server-side encryption using AWS KMS keys.
- **Standard-IA** — infrequent access, lower cost.
- **Subnet** — AZ-level network partition (public or private).
- **Trail** — configured log capture (all regions by default).

**Card 10:** Trusted Advisor · User / Group · VPC · VPC Endpoint

- **Trusted Advisor** — account-wide best-practice recommendations.
- **User / Group** — a person / a collection of users (groups can’t nest).
- **VPC** — regional private network.
- **VPC Endpoint** — private access to an AWS service from a VPC.

