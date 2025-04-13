import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Activity, User } from '@/types';
import ActivityCard from '@/components/itinerary/ActivityCard';
import { Button } from '@/components/ui/button';

const PublicItinerary: React.FC = () => {
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
        setActivities(activitiesData);

        const userId = JSON.parse(storedUser).id;
        const itineraryResponse = await fetch(`http://localhost:8000/itineraries/${userId}`);
        if (itineraryResponse.ok) {
          const itineraryData = await itineraryResponse.json();
          setPersonalActivities(itineraryData.activities);
        }
      } catch (err) {
        console.error(err);
        setError('Failed to load data. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [navigate]);

  const handleToggleActivity = async (activityId: string) => {
    if (!user) return;

    try {
      if (personalActivities.includes(activityId)) {
        await fetch(`http://localhost:8000/itineraries/${user.id}/activities/${activityId}`, {
          method: 'DELETE',
        });
        setPersonalActivities(prev => prev.filter(id => id !== activityId));
      } else {
        await fetch(`http://localhost:8000/itineraries/${user.id}/activities/${activityId}`, {
          method: 'POST',
        });
        setPersonalActivities(prev => [...prev, activityId]);
      }
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
        <h1 className="text-3xl font-bold">Bali Trip Public Itinerary</h1>
        <div className="space-x-2">
          <Button onClick={() => navigate('/personal-itinerary')}>
            View My Itinerary
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
        Browse the public itinerary and add activities to your personal itinerary.
      </p>

      {sortedDates.map(date => (
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
                  isInPersonalItinerary={personalActivities.includes(activity.id)}
                  onToggleActivity={handleToggleActivity}
                />
              ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default PublicItinerary;
