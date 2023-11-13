import logging
from args import args

logging.basicConfig(level=args.logLevel.upper())
logging.info('Logging now setup.')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
