import React, { useState } from 'react';
import { PaperInputForm } from './components/PaperInputForm';
import { ResultCard } from './components/ResultCard';
import { ResearchResult } from './types';
import { BookOpen, Loader2 } from 'lucide-react';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [results, setResults] = useState<ResearchResult | null>(null);
  const [analysis, setAnalysis] = useState<string | null>(null);

  const handlePaperSubmit = async ({ title, content }: { title: string; content: string }) => {
    setIsLoading(true);
    setError(null);
    
    try {
      // First analyze the content
      const analyzeResponse = await fetch('http://localhost:5003/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ paragraph: content }),
      });

      if (!analyzeResponse.ok) {
        throw new Error('Failed to analyze paper content');
      }

      const analyzeData = await analyzeResponse.json();
      setAnalysis(analyzeData.result);

      // Then get research results based on the title
      const researchResponse = await fetch('http://localhost:5001/api/research', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic: title }),
      });

      if (!researchResponse.ok) {
        throw new Error('Failed to fetch research results');
      }

      const researchData = await researchResponse.json();
      setResults(researchData);

      // The browser API will handle opening tabs and creating the Google Doc
      const allLinks = [...researchData.article_links, ...researchData.video_links];
      const browserResponse = await fetch('http://localhost:5002/api/browser', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ links: allLinks }),
      });

      if (!browserResponse.ok) {
        throw new Error('Failed to open browser tabs');
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-2 mb-4">
            <BookOpen className="text-blue-600" size={32} />
            <h1 className="text-3xl font-bold text-gray-900">Research Paper Analysis</h1>
          </div>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Input your research paper's title and content. We'll analyze the content, find relevant resources,
            and create a note-taking guide in a Google Doc.
          </p>
        </div>

        <div className="flex justify-center mb-8">
          <PaperInputForm onSubmit={handlePaperSubmit} isLoading={isLoading} />
        </div>

        {isLoading && (
          <div className="flex justify-center items-center gap-2 text-gray-600">
            <Loader2 className="animate-spin" size={24} />
            <span>Analyzing paper and gathering resources...</span>
          </div>
        )}

        {error && (
          <div className="text-center text-red-600 mb-8">
            {error}
          </div>
        )}

        {analysis && !isLoading && (
          <div className="max-w-4xl mx-auto mb-8">
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-xl font-semibold mb-4">Paper Analysis</h2>
              <div className="prose prose-blue">
                {analysis.split('\n').map((line, index) => (
                  <p key={index} className="mb-4">{line}</p>
                ))}
              </div>
            </div>
          </div>
        )}

        {results && !isLoading && (
          <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
            <ResultCard
              title="Research Articles"
              links={results.article_links}
              icon="article"
            />
            <ResultCard
              title="Educational Videos"
              links={results.video_links}
              icon="video"
            />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;