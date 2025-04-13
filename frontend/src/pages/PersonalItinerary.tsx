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
        const activitiesResponse = await fetch('http://localhost:8000/activities/');
        if (!activitiesResponse.ok) {
          throw new Error('Failed to fetch activities');
        }
        const activitiesData = await activitiesResponse.json();
        
        const userId = JSON.parse(storedUser).id;
        const itineraryResponse = await fetch(`http://localhost:8000/itineraries/${userId}`);
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
      await fetch(`http://localhost:8000/itineraries/${user.id}/activities/${activityId}`, {
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
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">My Bali Trip Itinerary</h1>
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
      
      <p className="mb-6 text-gray-600">
        Your personalized itinerary for the Bali trip.
      </p>

      {activities.length === 0 && !loading ? (
        <div className="text-center py-8">
          <p className="text-xl mb-4">You haven't added any activities to your itinerary yet.</p>
          <Button onClick={() => navigate('/public-itinerary')}>
            Browse Public Itinerary
          </Button>
        </div>
      ) : (
        sortedDates.map(date => (
          <div key={date} className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">
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
                    isInPersonalItinerary={true}
                    onToggleActivity={handleRemoveActivity}
                  />
                ))}
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default PersonalItinerary;
