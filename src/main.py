import os
   import arxiv
   from openai import OpenAI

   client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "sk-your-key-here"))
   MODEL_NAME = "gpt-4o-mini"

   class PaperMindAgentSystem:
       def __init__(self, keyword: str):
           self.keyword = keyword
           self.papers = []

       def run_search_agent(self):
           print(f"🔍 [Search Agent] '{self.keyword}' 관련 최신 논문 검색 중...")
           search = arxiv.Search(query=self.keyword, max_results=3, sort_by=arxiv.SortCriterion.SubmittedDate)
           for result in search.results():
               self.papers.append({"title": result.title, "summary": result.summary, "date": result.published.strftime("%Y-%m-%d")})

       def run_analyst_agent(self) -> str:
           print("🧠 [Analyst Agent] 방법론 및 기여점 분석 중...")
           combined_summary = ""
           for i, p in enumerate(self.papers):
               prompt = f"논문 제목: {p['title']}\n초록: {p['summary']}\n이 논문의 핵심 기여점을 요약해줘."
               res = client.chat.completions.create(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
               combined_summary += f"\n[{i+1}] {p['title']}\n- 요약: {res.choices[0].message.content}\n"
           return combined_summary

       def run_writer_agent(self, analysis: str):
           print("✍️ [Writer Agent] 마크다운 리포트 생성 중...")
           os.makedirs("output", exist_ok=True)
           with open(f"output/lineage_report.md", "w", encoding="utf-8") as f:
               f.write(f"# Research Lineage Report\n\n{analysis}")

   if __name__ == "__main__":
       # 초기 실행 키워드
       system = PaperMindAgentSystem(keyword="Spiking Neural Networks DDPM")
       system.run_search_agent()
       analysis = system.run_analyst_agent()
       system.run_writer_agent(analysis)
