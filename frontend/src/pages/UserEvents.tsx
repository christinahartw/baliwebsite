import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { Dialog, DialogContent, DialogTrigger } from '@/components/ui/dialog';
import CreateEventForm from '@/components/events/CreateEventForm';
import EventCard from '@/components/events/EventCard';
import { User } from '@/types';

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

const UserEvents: React.FC = () => {
  const [events, setEvents] = useState<UserEvent[]>([]);
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (!storedUser) {
      navigate('/');
      return;
    }

    setUser(JSON.parse(storedUser));
    
    const fetchEvents = async () => {
      try {
        const response = await fetch('https://app-qfmuihch.fly.dev/events/');
        if (!response.ok) {
          throw new Error('Failed to fetch events');
        }
        const data = await response.json();
        setEvents(data);
      } catch (err) {
        console.error(err);
        setError('Failed to load events. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchEvents();
  }, [navigate]);

  const handleCreateEvent = async (eventData: {
    title: string;
    description: string;
    date: string;
    time: string;
    link?: string;
  }) => {
    if (!user) return;

    try {
      const response = await fetch('https://app-qfmuihch.fly.dev/events/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: eventData.title,
          description: eventData.description,
          date: eventData.date,  // ISO format YYYY-MM-DD
          time: eventData.time,  // HH:MM format
          link: eventData.link,
          user_id: user.id,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to create event');
      }

      const newEvent = await response.json();
      setEvents(prev => [...prev, newEvent]);
      setIsDialogOpen(false);
    } catch (err) {
      console.error(err);
      setError('Failed to create event. Please try again.');
    }
  };

  const handleDeleteEvent = async (eventId: string) => {
    if (!user) return;

    try {
      const response = await fetch(`https://app-qfmuihch.fly.dev/events/${eventId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: user.id,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to delete event');
      }

      setEvents(prev => prev.filter(event => event.id !== eventId));
    } catch (err) {
      console.error(err);
      setError('Failed to delete event. Please try again.');
    }
  };

  const sortedEvents = [...events].sort((a, b) => {
    const dateA = new Date(a.date);
    const dateB = new Date(b.date);
    if (dateA.getTime() !== dateB.getTime()) {
      return dateA.getTime() - dateB.getTime();
    }
    return a.time.localeCompare(b.time);
  });

  if (loading) {
    return <div className="container mx-auto p-4 text-center">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-accent/10 to-primary/10 pb-8">
      <div className="container mx-auto p-4">
        <div className="flex flex-col md:flex-row justify-between items-center mb-6 bg-accent/20 p-4 rounded-lg shadow-sm">
          <h1 className="text-3xl font-bold text-accent-foreground mb-4 md:mb-0">User-Created Events</h1>
          <div className="space-x-2">
            <Button onClick={() => navigate('/public-itinerary')}>
              View Public Itinerary
            </Button>
            <Button variant="outline" onClick={() => navigate('/personal-itinerary')}>
              View My Itinerary
            </Button>
          </div>
        </div>
        
        <div className="mb-6 bg-white/50 p-4 rounded-lg shadow-sm border border-accent/20 flex justify-between items-center">
          <p className="text-muted-foreground">
            Browse events created by other users or create your own event.
          </p>
          <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
            <DialogTrigger asChild>
              <Button>Create New Event</Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-md">
              <CreateEventForm 
                onSubmit={handleCreateEvent} 
                onCancel={() => setIsDialogOpen(false)} 
              />
            </DialogContent>
          </Dialog>
        </div>

        {error && (
          <div className="mb-6 p-4 bg-destructive/10 border border-destructive rounded-md text-destructive">
            {error}
          </div>
        )}

        {sortedEvents.length === 0 ? (
          <div className="text-center py-12 bg-white/50 rounded-lg shadow-sm border border-accent/20">
            <p className="text-xl mb-4 text-muted-foreground">No user events have been created yet.</p>
            <p className="text-muted-foreground mb-4">Be the first to create an event for others to join!</p>
            <Button onClick={() => setIsDialogOpen(true)}>
              Create New Event
            </Button>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {sortedEvents.map(event => (
              <EventCard
                key={event.id}
                event={event}
                isCreator={user?.id === event.user_id}
                onDelete={user?.id === event.user_id ? handleDeleteEvent : undefined}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default UserEvents;
