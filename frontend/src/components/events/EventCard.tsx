import React from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { ExternalLink } from 'lucide-react';

interface UserEvent {
  id: string;
  user_id: string;
  title: string;
  description: string;
  date: string;
  time: string;
  link?: string;
  created_at?: string;
}

interface EventCardProps {
  event: UserEvent;
  isCreator: boolean;
  onDelete?: (eventId: string) => Promise<void>;
}

const EventCard: React.FC<EventCardProps> = ({ 
  event, 
  isCreator,
  onDelete
}) => {
  const formattedDate = new Date(event.date + 'T00:00:00Z').toLocaleDateString('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric'
  });

  const handleDelete = async () => {
    if (onDelete) {
      await onDelete(event.id);
    }
  };

  return (
    <Card className="mb-4 border-2 border-accent/30 hover:border-accent/50 transition-all">
      <CardHeader className="bg-accent/10 rounded-t-lg">
        <CardTitle className="text-xl">{event.title}</CardTitle>
        <CardDescription className="text-sm font-medium">
          {formattedDate} at {event.time}
        </CardDescription>
      </CardHeader>
      <CardContent className="pt-4">
        <p className="text-sm">{event.description}</p>
        
        {event.link && (
          <div className="mt-3">
            <a 
              href={event.link} 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center text-primary hover:underline text-sm"
            >
              <ExternalLink className="h-4 w-4 mr-1" />
              Event Link
            </a>
          </div>
        )}
      </CardContent>
      {isCreator && onDelete && (
        <CardFooter>
          <Button 
            variant="destructive"
            onClick={handleDelete}
            className="w-full"
            size="sm"
          >
            Delete Event
          </Button>
        </CardFooter>
      )}
    </Card>
  );
};

export default EventCard;
