import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.connectivity import GraphQLQueryStep

def main():
    pipeline = Pipeline(pipeline_name="GraphQL_Demo", verbose=True)

    # Example using Countries GraphQL API
    query = """
    query getCountry($code: ID!) {
      country(code: $code) {
        name
        native
        capital
        emoji
        currency
        languages {
          code
          name
        }
      }
    }
    """
    
    fetch_country = GraphQLQueryStep.as_step(
        name="Fetch_Country_Data",
        url="https://countries.trevorblades.com/",
        query=query,
        variables={"code": "ES"},
        response_key="country_info"
    )

    pipeline.set_steps([
        fetch_country,
        lambda d: print(f"\n🌍 Country: {d['country_info']['data']['country']['name']} {d['country_info']['data']['country']['emoji']}") or d
    ])

    pipeline.run({})

if __name__ == "__main__":
    main()
