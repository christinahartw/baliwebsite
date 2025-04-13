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

  const getCategoryColor = (category: string) => {
    switch(category.toLowerCase()) {
      case 'hiking':
        return 'bg-green-200 text-green-800';
      case 'nature':
        return 'bg-emerald-200 text-emerald-800';
      case 'sightseeing':
        return 'bg-blue-200 text-blue-800';
      case 'cultural':
        return 'bg-purple-200 text-purple-800';
      case 'tour':
        return 'bg-yellow-200 text-yellow-800';
      case 'adventure':
        return 'bg-orange-200 text-orange-800';
      case 'recreation':
        return 'bg-cyan-200 text-cyan-800';
      case 'relaxation':
        return 'bg-indigo-200 text-indigo-800';
      case 'shopping':
        return 'bg-pink-200 text-pink-800';
      case 'dining':
        return 'bg-red-200 text-red-800';
      default:
        return 'bg-gray-200 text-gray-800';
    }
  };

  return (
    <Card className="mb-4 border-2 border-primary/20 hover:border-primary/40 transition-all">
      <CardHeader className="bg-primary/10 rounded-t-lg">
        <CardTitle className="text-xl">{activity.title}</CardTitle>
        <CardDescription className="text-sm font-medium">
          {formattedDate} at {formattedTime}
        </CardDescription>
      </CardHeader>
      <CardContent className="pt-4">
        <p className="text-sm">{activity.description}</p>
        <div className="mt-3 flex flex-col gap-2">
          <div className="flex items-center text-sm">
            <span className="font-medium w-20">Location:</span>
            <span className="ml-2">{activity.location}</span>
          </div>
          <div className="flex items-center text-sm">
            <span className="font-medium w-20">Category:</span>
            <span className={`ml-2 px-2 py-0.5 rounded-full text-xs ${getCategoryColor(activity.category)}`}>
              {activity.category}
            </span>
          </div>
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
