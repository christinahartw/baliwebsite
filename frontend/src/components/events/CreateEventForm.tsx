import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Label } from '@/components/ui/label';

interface CreateEventFormProps {
  onSubmit: (eventData: {
    title: string;
    description: string;
    date: string;
    time: string;
    link?: string;
  }) => Promise<void>;
  onCancel: () => void;
}

const CreateEventForm: React.FC<CreateEventFormProps> = ({ onSubmit, onCancel }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [link, setLink] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!title || !description || !date || !time) {
      setError('Please fill in all required fields');
      return;
    }

    setLoading(true);
    setError('');

    try {
      await onSubmit({
        title,
        description,
        date,
        time,
        link: link || undefined
      });
    } catch (err) {
      console.error(err);
      setError('Failed to create event. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="w-full max-w-md mx-auto border-2 border-primary/30 shadow-lg">
      <CardHeader className="bg-primary/10 rounded-t-lg">
        <CardTitle className="text-center text-xl">Create New Event</CardTitle>
      </CardHeader>
      <form onSubmit={handleSubmit}>
        <CardContent className="pt-6 space-y-4">
          <div className="space-y-2">
            <Label htmlFor="title">Title *</Label>
            <Input
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Event title"
              required
              className="border-2 border-primary/30 focus:border-primary/50"
            />
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="description">Description *</Label>
            <Textarea
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Event description"
              required
              className="min-h-[100px] border-2 border-primary/30 focus:border-primary/50"
            />
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="date">Date *</Label>
              <Input
                id="date"
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
                min="2025-04-18"
                max="2025-04-24"
                required
                className="border-2 border-primary/30 focus:border-primary/50"
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="time">Time *</Label>
              <Input
                id="time"
                type="time"
                value={time}
                onChange={(e) => setTime(e.target.value)}
                required
                className="border-2 border-primary/30 focus:border-primary/50"
              />
            </div>
          </div>
          
          <div className="space-y-2">
            <Label htmlFor="link">Link (Optional)</Label>
            <Input
              id="link"
              type="url"
              value={link}
              onChange={(e) => setLink(e.target.value)}
              placeholder="https://example.com"
              className="border-2 border-primary/30 focus:border-primary/50"
            />
          </div>
          
          {error && <p className="text-sm text-destructive">{error}</p>}
        </CardContent>
        
        <CardFooter className="flex justify-between space-x-2 bg-accent/10 rounded-b-lg">
          <Button 
            type="button" 
            variant="outline" 
            onClick={onCancel}
            disabled={loading}
          >
            Cancel
          </Button>
          <Button 
            type="submit" 
            disabled={loading}
          >
            {loading ? 'Creating...' : 'Create Event'}
          </Button>
        </CardFooter>
      </form>
    </Card>
  );
};

export default CreateEventForm;
