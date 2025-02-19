from crunpyroll import types
import crunpyroll

class GetIndex:
    def get_index(
        self: "crunpyroll.Client",
    ) -> "types.SessionIndex":
        """
        Get session index. It's unlikely that you would use this method.

        Returns:
            :obj:`~crunpyroll.types.SessionIndex`:
                On success, informations about session index are returned.
        """
        self.session.retrieve()
        response = self.api_request(
            method="GET",
            endpoint="index/v2",
        )
        return types.SessionIndex(response)
