from crunpyroll import types
import crunpyroll

class GetManifest:
    def get_manifest(
        self: "crunpyroll.Client",
        url: str
    ) -> "types.Manifest":
        """
        Retrieve and parse manifest.

        Parameters:
            url (``str``):
                URL of the manifest.

        Returns:
            :obj:`~crunpyroll.types.Manifest`:
                On success, parsed manifest is returned.
        """
        self.session.retrieve()
        response = self.manifest_request(url)
        return types.Manifest.parse(response)
