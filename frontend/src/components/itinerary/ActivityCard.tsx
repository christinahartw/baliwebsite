import React from 'react';
import { Activity } from '@/types';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';

interface ActivityCardProps {
  activity: Activity;
  isInPersonalItinerary: boolean;
  onToggleActivity: (activityId: string) => void;
}

const ActivityCard: React.FC<ActivityCardProps> = ({ 
  activity, 
  isInPersonalItinerary, 
  onToggleActivity 
}) => {
  const formattedDate = new Date(activity.date).toLocaleDateString('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric'
  });

  const formattedTime = activity.time;

  return (
    <Card className="mb-4">
      <CardHeader>
        <CardTitle>{activity.title}</CardTitle>
        <CardDescription>
          {formattedDate} at {formattedTime}
        </CardDescription>
      </CardHeader>
      <CardContent>
        <p>{activity.description}</p>
        <div className="mt-2 flex items-center text-sm">
          <span className="font-medium">Location:</span>
          <span className="ml-2">{activity.location}</span>
        </div>
        <div className="mt-1 flex items-center text-sm">
          <span className="font-medium">Category:</span>
          <span className="ml-2">{activity.category}</span>
        </div>
      </CardContent>
      <CardFooter>
        <Button 
          variant={isInPersonalItinerary ? "destructive" : "default"}
          onClick={() => onToggleActivity(activity.id)}
          className="w-full"
        >
          {isInPersonalItinerary ? "Remove from My Itinerary" : "Add to My Itinerary"}
        </Button>
      </CardFooter>
    </Card>
  );
};

export default ActivityCard;
