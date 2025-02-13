export interface ResearchResult {
  article_links: string[];
  video_links: string[];
}

export interface ResearchResponse {
  status: string;
  data?: ResearchResult;
  error?: string;
}

export interface PaperInput {
  title: string;
  content: string;
}

export interface AnalysisResult {
  result: string;
}