"""Split documents into RAG-ready chunks (with page numbers) and write them to a JSONL file.

Load chunks.jsonl into any vector database: Pinecone, Qdrant, Chroma, pgvector, etc.

Usage:
    python rag_chunks.py https://example.com/handbook.pdf --size 1200
"""
import argparse
import json
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("urls", nargs="+")
parser.add_argument("--size", type=int, default=1200, help="Chunk size in characters (800-1500 suits most embedding models)")
args = parser.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fguiraud/document-to-markdown-tables").call(run_input={
    "sources": [{"url": u} for u in args.urls],
    "outputs": ["chunks"],
    "chunkSize": args.size,
    "removeHeadersFooters": True,  # repeated page headers/footers would pollute every chunk
})

count = 0
with open("chunks.jsonl", "w", encoding="utf-8") as f:
    for doc in client.dataset(run.default_dataset_id).iterate_items():
        for chunk in doc.get("chunks") or []:
            record = {
                "id": f"{doc['source']}#{chunk['index']}",
                "text": chunk["text"],
                "metadata": {"source": doc["source"], "pageStart": chunk.get("pageStart"), "pageEnd": chunk.get("pageEnd")},
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
print(f"Wrote {count} chunks to chunks.jsonl")
