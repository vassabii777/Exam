import pandas as pd
from rectools.models          import PopularModel
from rectools.dataset         import Dataset
from recommendations.models   import UserTrackInteraction
from tracks.models            import Track  


def get_track_recommendations(user_id, n_recommendations=5):
    interactions = UserTrackInteraction.objects.all().values('user_id', 'track_id', 'rating')

    df = pd.DataFrame(list(interactions))

    dataset = Dataset.construct(
        interactions_df=df,
        user_col = "user_id",
        item_col = 'track_id',
        weight_col = 'rating'
    )

    model = PopularModel()
    model.fit(dataset)

    recommendations = model.recommend(
        users=[user_id],
        dataset=dataset,
        k=n_recommendations
    )
    track_ids= recommendations[0]["item_id"].tolist()

    return Track.objects.filter(id__n = track_ids)
