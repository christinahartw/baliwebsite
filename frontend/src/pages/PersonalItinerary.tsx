import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Activity, User } from '@/types';
import ActivityCard from '@/components/itinerary/ActivityCard';
import { Button } from '@/components/ui/button';

const PersonalItinerary: React.FC = () => {
  const [activities, setActivities] = useState<Activity[]>([]);
  const [personalActivities, setPersonalActivities] = useState<string[]>([]);
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (!storedUser) {
      navigate('/');
      return;
    }

    setUser(JSON.parse(storedUser));
    
    const fetchData = async () => {
      try {
        const activitiesResponse = await fetch('https://app-qfmuihch.fly.dev/activities/');
        if (!activitiesResponse.ok) {
          throw new Error('Failed to fetch activities');
        }
        const activitiesData = await activitiesResponse.json();
        
        const userId = JSON.parse(storedUser).id;
        const itineraryResponse = await fetch(`https://app-qfmuihch.fly.dev/itineraries/${userId}`);
        if (!itineraryResponse.ok) {
          throw new Error('Failed to fetch personal itinerary');
        }
        
        const itineraryData = await itineraryResponse.json();
        setPersonalActivities(itineraryData.activities);
        
        const personalActivitiesData = activitiesData.filter(
          (activity: Activity) => itineraryData.activities.includes(activity.id)
        );
        
        setActivities(personalActivitiesData);
      } catch (err) {
        console.error(err);
        setError('Failed to load data. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [navigate]);

  const handleRemoveActivity = async (activityId: string) => {
    if (!user) return;

    try {
      await fetch(`https://app-qfmuihch.fly.dev/itineraries/${user.id}/activities/${activityId}`, {
        method: 'DELETE',
      });
      
      setPersonalActivities(prev => prev.filter(id => id !== activityId));
      setActivities(prev => prev.filter(activity => activity.id !== activityId));
    } catch (err) {
      console.error(err);
      setError('Failed to update itinerary. Please try again.');
    }
  };

  const groupedActivities = activities.reduce((groups, activity) => {
    const date = activity.date;
    if (!groups[date]) {
      groups[date] = [];
    }
    groups[date].push(activity);
    return groups;
  }, {} as Record<string, Activity[]>);

  const sortedDates = Object.keys(groupedActivities).sort();

  if (loading) {
    return <div className="container mx-auto p-4 text-center">Loading...</div>;
  }

  if (error) {
    return <div className="container mx-auto p-4 text-center text-red-500">{error}</div>;
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-secondary/10 to-accent/10 pb-8">
      <div className="container mx-auto p-4">
        <div className="flex flex-col md:flex-row justify-between items-center mb-6 bg-secondary/20 p-4 rounded-lg shadow-sm">
          <h1 className="text-3xl font-bold text-secondary-foreground mb-4 md:mb-0">My Bali Trip Itinerary</h1>
          <div className="space-x-2">
            <Button onClick={() => navigate('/public-itinerary')}>
              View Public Itinerary
            </Button>
            <Button variant="outline" onClick={() => {
              localStorage.removeItem('user');
              navigate('/');
            }}>
              Sign Out
            </Button>
          </div>
        </div>
        
        <p className="mb-6 text-muted-foreground bg-white/50 p-3 rounded-md shadow-sm border border-secondary/20 text-center">
          Your personalized itinerary for the Bali trip.
        </p>

      {activities.length === 0 && !loading ? (
        <div className="text-center py-12 bg-white/50 rounded-lg shadow-sm border border-secondary/20">
          <p className="text-xl mb-4 text-muted-foreground">You haven't added any activities to your itinerary yet.</p>
          <Button onClick={() => navigate('/public-itinerary')}>
            Browse Public Itinerary
          </Button>
        </div>
      ) : (
        sortedDates.map(date => (
          <div key={date} className="mb-8 bg-white/50 p-4 rounded-lg shadow-sm border border-secondary/20">
            <h2 className="text-2xl font-semibold mb-4 text-secondary-foreground">
              {new Date(date).toLocaleDateString('en-US', {
                weekday: 'long',
                month: 'long',
                day: 'numeric',
                year: 'numeric'
              })}
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {groupedActivities[date]
                .sort((a, b) => a.time.localeCompare(b.time))
                .map(activity => (
                  <ActivityCard
                    key={activity.id}
                    activity={activity}
                    isInPersonalItinerary={personalActivities.includes(activity.id)}
                    onToggleActivity={handleRemoveActivity}
                  />
                ))}
            </div>
          </div>
        ))
      )}
      </div>
    </div>
  );
};

export default PersonalItinerary;
