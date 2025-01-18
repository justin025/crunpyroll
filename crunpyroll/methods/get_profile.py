from crunpyroll import types
import crunpyroll

class GetProfile:
    def get_profile(
        self: "crunpyroll.Client",
    ) -> "types.Profile":
        """
        Get current profile informations.

        Returns:
            :obj:`~crunpyroll.types.Profile`:
                On success, profile object is returned.
        """
        self.session.retrieve()
        response = self.api_request(
            method="GET",
            endpoint="accounts/v1/me/profile",
        )
        return types.Profile(response)
