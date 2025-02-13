import React from 'react';
import { ExternalLink, FileText, Video } from 'lucide-react';

interface ResultCardProps {
  title: string;
  links: string[];
  icon: 'article' | 'video';
}

export function ResultCard({ title, links, icon }: ResultCardProps) {
  const Icon = icon === 'article' ? FileText : Video;

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex items-center gap-2 mb-4">
        <Icon className="text-blue-600" size={24} />
        <h2 className="text-xl font-semibold">{title}</h2>
      </div>
      <ul className="space-y-3">
        {links.map((link, index) => (
          <li key={index} className="flex items-start gap-2">
            <ExternalLink className="flex-shrink-0 mt-1 text-gray-400" size={16} />
            <a
              href={link}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:text-blue-800 hover:underline break-all"
            >
              {link}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}